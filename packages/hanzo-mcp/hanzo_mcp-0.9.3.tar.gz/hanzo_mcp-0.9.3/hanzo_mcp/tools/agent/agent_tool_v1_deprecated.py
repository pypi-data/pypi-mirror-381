"""Agent tool implementation for Hanzo AI.

This module implements the AgentTool that allows Claude to delegate tasks to sub-agents,
enabling concurrent execution of multiple operations and specialized processing.
"""

import re
import json
import time
import asyncio

# Import litellm with warnings suppressed
import warnings
from typing import Unpack, Annotated, TypedDict, final, override
from collections.abc import Iterable

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    import litellm
from pydantic import Field
from mcp.server import FastMCP

from hanzo_mcp.tools.common.auto_timeout import auto_timeout
from openai.types.chat import ChatCompletionToolParam, ChatCompletionMessageParam
from mcp.server.fastmcp import Context as MCPContext

from hanzo_mcp.tools.jupyter import get_read_only_jupyter_tools
from hanzo_mcp.tools.filesystem import Edit, MultiEdit, get_read_only_filesystem_tools
from hanzo_mcp.tools.common.base import BaseTool
from hanzo_mcp.tools.agent.prompt import (
    get_default_model,
    get_system_prompt,
    get_model_parameters,
    get_allowed_agent_tools,
)
from hanzo_mcp.tools.common.context import (
    ToolContext,
    create_tool_context,
)
from hanzo_mcp.tools.agent.critic_tool import CriticTool, CriticProtocol
from hanzo_mcp.tools.agent.iching_tool import IChingTool
from hanzo_mcp.tools.agent.review_tool import ReviewTool, ReviewProtocol
from hanzo_mcp.tools.common.batch_tool import BatchTool
from hanzo_mcp.tools.agent.tool_adapter import (
    convert_tools_to_openai_functions,
)
from hanzo_mcp.tools.common.permissions import PermissionManager
from hanzo_mcp.tools.agent.clarification_tool import ClarificationTool
from hanzo_mcp.tools.agent.clarification_protocol import (
    ClarificationType,
    AgentClarificationMixin,
)

Prompt = Annotated[
    str,
    Field(
        description="Task for the agent to perform (must include absolute paths starting with /)",
        min_length=1,
    ),
]


class AgentToolParams(TypedDict, total=False):
    """Parameters for the AgentTool.

    Attributes:
        prompts: Task(s) for the agent to perform (must include absolute paths starting with /)
    """

    prompts: str | list[str]


@final
class AgentTool(AgentClarificationMixin, BaseTool):
    """Tool for delegating tasks to sub-agents.

    The AgentTool allows Claude to create and manage sub-agents for performing
    specialized tasks concurrently, such as code search, analysis, and more.

    Agents can request clarification from the main loop up to once per task.
    """

    @property
    @override
    def name(self) -> str:
        """Get the tool name.

        Returns:
            Tool name
        """
        return "agent"

    @property
    @override
    def description(self) -> str:
        """Get the tool description.

        Returns:
            Tool description
        """
        # TODO: Add glob when it is implemented
        at = [t.name for t in self.available_tools]

        return f"""Launch a new agent that has access to the following tools: {at}. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries, use the Agent tool to perform the search for you.

When to use the Agent tool:
- If you are searching for a keyword like \"config\" or \"logger\", or for questions like \"which file does X?\", the Agent tool is strongly recommended
- When you need to perform edits across multiple files based on search results
- When you need to delegate complex file modification tasks

When NOT to use the Agent tool:
- If you want to read a specific file path, use the read or glob tool instead of the Agent tool, to find the match more quickly
- If you are searching for a specific class definition like \"class Foo\", use the glob tool instead, to find the match more quickly
- If you are searching for code within a specific file or set of 2-3 files, use the read tool instead of the Agent tool, to find the match more quickly
- Writing code and running bash commands (use other tools for that)
- Other tasks that are not related to searching for a keyword or file

Usage notes:
1. Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a single message with multiple tool uses
2. When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.
3. Each agent invocation is stateless. You will not be able to send additional messages to the agent, nor will the agent be able to communicate with you outside of its final report. Therefore, your prompt should contain a highly detailed task description for the agent to perform autonomously and you should specify exactly what information the agent should return back to you in its final and only message to you.
4. The agent's outputs should generally be trusted
5. Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since it is not aware of the user's intent"""

    def __init__(
        self,
        permission_manager: PermissionManager,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        max_tokens: int | None = None,
        max_iterations: int = 10,
        max_tool_uses: int = 30,
    ) -> None:
        """Initialize the agent tool.

        Args:

            permission_manager: Permission manager for access control
            model: Optional model name override in LiteLLM format (e.g., "openai/gpt-4o")
            api_key: Optional API key for the model provider
            base_url: Optional base URL for the model provider API endpoint
            max_tokens: Optional maximum tokens for model responses
            max_iterations: Maximum number of iterations for agent (default: 10)
            max_tool_uses: Maximum number of total tool uses for agent (default: 30)
        """

        self.permission_manager = permission_manager
        self.model_override = model
        self.api_key_override = api_key
        self.base_url_override = base_url
        self.max_tokens_override = max_tokens
        self.max_iterations = max_iterations
        self.max_tool_uses = max_tool_uses
        self.available_tools: list[BaseTool] = []
        self.available_tools.extend(get_read_only_filesystem_tools(self.permission_manager))
        self.available_tools.extend(get_read_only_jupyter_tools(self.permission_manager))

        # Always add edit tools - agents should have edit access
        self.available_tools.append(Edit(self.permission_manager))
        self.available_tools.append(MultiEdit(self.permission_manager))

        # Add clarification tool for agents
        self.available_tools.append(ClarificationTool())

        # Add critic tool for agents (devil's advocate)
        self.available_tools.append(CriticTool())

        # Add review tool for agents (balanced review)
        self.available_tools.append(ReviewTool())

        # Add I Ching tool for creative guidance
        self.available_tools.append(IChingTool())

        self.available_tools.append(BatchTool({t.name: t for t in self.available_tools}))

        # Initialize protocols
        self.critic_protocol = CriticProtocol()
        self.review_protocol = ReviewProtocol()

    @override
    @auto_timeout("agent_tool_v1_deprecated")


    async def call(
        self,
        ctx: MCPContext,
        **params: Unpack[AgentToolParams],
    ) -> str:
        """Execute the tool with the given parameters.

        Args:
            ctx: MCP context
            **params: Tool parameters

        Returns:
            Tool execution result
        """
        start_time = time.time()

        # Create tool context
        tool_ctx = create_tool_context(ctx)
        await tool_ctx.set_tool_info(self.name)

        # Extract and validate parameters
        prompts = params.get("prompts")

        if prompts is None:
            await tool_ctx.error("No prompts provided")
            return """Error: At least one prompt must be provided.

IMPORTANT REMINDER FOR CLAUDE:
The dispatch_agent tool requires prompts parameter. Please provide either:
- A single prompt as a string
- Multiple prompts as an array of strings

Each prompt must contain absolute paths starting with /.
Example of correct usage:
- prompts: "Search for all instances of the 'config' variable in /Users/bytedance/project/hanzo-mcp"
- prompts: ["Find files in /path/to/project", "Search code in /path/to/src"]"""

        # Handle both string and list inputs
        if isinstance(prompts, str):
            prompt_list = [prompts]
        elif isinstance(prompts, list):
            if not prompts:
                await tool_ctx.error("Empty prompts list provided")
                return "Error: At least one prompt must be provided when using a list."
            if not all(isinstance(p, str) for p in prompts):
                await tool_ctx.error("All prompts must be strings")
                return "Error: All prompts in the list must be strings."
            prompt_list = prompts
        else:
            await tool_ctx.error("Invalid prompts parameter type")
            return "Error: Parameter 'prompts' must be a string or an array of strings."

        # Validate absolute paths in all prompts
        absolute_path_pattern = r"/(?:[^/\s]+/)*[^/\s]+"
        for prompt in prompt_list:
            if not re.search(absolute_path_pattern, prompt):
                await tool_ctx.error(f"Prompt does not contain absolute path: {prompt[:50]}...")
                return """Error: All prompts must contain at least one absolute path.

IMPORTANT REMINDER FOR CLAUDE:
When using the dispatch_agent tool, always include absolute paths in your prompts.
Example of correct usage:
- "Search for all instances of the 'config' variable in /Users/bytedance/project/hanzo-mcp"
- "Find files that import the database module in /Users/bytedance/project/hanzo-mcp/src"

The agent cannot access files without knowing their absolute locations."""

        # Execute agent(s) - always use _execute_multiple_agents for list inputs
        if len(prompt_list) == 1:
            await tool_ctx.info("Launching agent")
            result = await self._execute_multiple_agents(prompt_list, tool_ctx)
            execution_time = time.time() - start_time
            formatted_result = f"""Agent execution completed in {execution_time:.2f} seconds.

AGENT RESPONSE:
{result}"""
            await tool_ctx.info(f"Agent execution completed in {execution_time:.2f}s")
            return formatted_result
        else:
            await tool_ctx.info(f"Launching {len(prompt_list)} agents in parallel")
            result = await self._execute_multiple_agents(prompt_list, tool_ctx)
            execution_time = time.time() - start_time
            formatted_result = f"""Multi-agent execution completed in {execution_time:.2f} seconds ({len(prompt_list)} agents).

AGENT RESPONSES:
{result}"""
            await tool_ctx.info(f"Multi-agent execution completed in {execution_time:.2f}s")
            return formatted_result

    async def _execute_agent(self, prompt: str, tool_ctx: ToolContext) -> str:
        """Execute a single agent with the given prompt.

        Args:
            prompt: The task prompt for the agent
            tool_ctx: Tool context for logging

        Returns:
            Agent execution result
        """
        # Get available tools for the agent
        agent_tools = get_allowed_agent_tools(
            self.available_tools,
            self.permission_manager,
        )

        # Convert tools to OpenAI format
        openai_tools = convert_tools_to_openai_functions(agent_tools)

        # Log execution start
        await tool_ctx.info("Starting agent execution")

        # Create a result container
        result = ""

        try:
            # Create system prompt for this agent
            system_prompt = get_system_prompt(
                agent_tools,
                self.permission_manager,
            )

            # Execute agent
            await tool_ctx.info(f"Executing agent task: {prompt[:50]}...")
            result = await self._execute_agent_with_tools(system_prompt, prompt, agent_tools, openai_tools, tool_ctx)
        except Exception as e:
            # Log and return error result
            error_message = f"Error executing agent: {str(e)}"
            await tool_ctx.error(error_message)
            return f"Error: {error_message}"

        return result if result else "No results returned from agent"

    async def _execute_multiple_agents(self, prompts: list[str], tool_ctx: ToolContext) -> str:
        """Execute multiple agents concurrently.

        Args:
            prompts: List of prompts for the agents
            tool_ctx: Tool context for logging

        Returns:
            Combined results from all agents
        """
        # Get available tools for the agents
        agent_tools = get_allowed_agent_tools(
            self.available_tools,
            self.permission_manager,
        )

        # Convert tools to OpenAI format
        openai_tools = convert_tools_to_openai_functions(agent_tools)

        # Create system prompt for the agents
        system_prompt = get_system_prompt(
            agent_tools,
            self.permission_manager,
        )

        # Create tasks for parallel execution
        tasks = []
        for i, prompt in enumerate(prompts):
            await tool_ctx.info(f"Creating agent task {i + 1}: {prompt[:50]}...")
            task = self._execute_agent_with_tools(system_prompt, prompt, agent_tools, openai_tools, tool_ctx)
            tasks.append(task)

        # Execute all agents concurrently
        await tool_ctx.info(f"Executing {len(tasks)} agents in parallel")
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Handle single agent case
        if len(results) == 1:
            if isinstance(results[0], Exception):
                await tool_ctx.error(f"Agent execution failed: {str(results[0])}")
                return f"Error: {str(results[0])}"
            return results[0]

        # Format results for multiple agents
        formatted_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                formatted_results.append(f"Agent {i + 1} Error:\n{str(result)}")
                await tool_ctx.error(f"Agent {i + 1} failed: {str(result)}")
            else:
                formatted_results.append(f"Agent {i + 1} Result:\n{result}")

        return "\n\n---\n\n".join(formatted_results)

    async def _execute_agent_with_tools(
        self,
        system_prompt: str,
        user_prompt: str,
        available_tools: list[BaseTool],
        openai_tools: list[ChatCompletionToolParam],
        tool_ctx: ToolContext,
    ) -> str:
        """Execute agent with tool handling.

        Args:
            system_prompt: System prompt for the agent
            user_prompt: User prompt for the agent
            available_tools: List of available tools
            openai_tools: List of tools in OpenAI format
            tool_ctx: Tool context for logging

        Returns:
            Agent execution result
        """
        # Get model parameters and name
        model = get_default_model(self.model_override)
        params = get_model_parameters(max_tokens=self.max_tokens_override)

        # Initialize messages
        messages: Iterable[ChatCompletionMessageParam] = []
        messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_prompt})

        # Track tool usage for metrics
        tool_usage = {}
        total_tool_use_count = 0
        iteration_count = 0
        max_tool_uses = self.max_tool_uses  # Safety limit to prevent infinite loops
        max_iterations = self.max_iterations  # Add a maximum number of iterations for safety

        # Execute until the agent completes or reaches the limit
        while total_tool_use_count < max_tool_uses and iteration_count < max_iterations:
            iteration_count += 1
            await tool_ctx.info(f"Calling model (iteration {iteration_count})...")

            try:
                # Configure model parameters based on capabilities
                completion_params = {
                    "model": model,
                    "messages": messages,
                    "tools": openai_tools,
                    "tool_choice": "auto",
                    "temperature": params["temperature"],
                    "timeout": params["timeout"],
                }

                if self.api_key_override:
                    completion_params["api_key"] = self.api_key_override

                # Add max_tokens if provided
                if params.get("max_tokens"):
                    completion_params["max_tokens"] = params.get("max_tokens")

                # Add base_url if provided
                if self.base_url_override:
                    completion_params["base_url"] = self.base_url_override

                # Make the model call
                response = litellm.completion(**completion_params)  # pyright: ignore

                if len(response.choices) == 0:  # pyright: ignore
                    raise ValueError("No response choices returned")

                message = response.choices[0].message  # pyright: ignore

                # Add message to conversation history
                messages.append(message)  # pyright: ignore

                # If no tool calls, we're done
                if not message.tool_calls:
                    return message.content or "Agent completed with no response."

                # Process tool calls
                tool_call_count = len(message.tool_calls)
                await tool_ctx.info(f"Processing {tool_call_count} tool calls")

                # Track which tool calls we've processed to ensure all get results
                tool_results_to_add = []

                for tool_call in message.tool_calls:
                    total_tool_use_count += 1
                    function_name = tool_call.function.name

                    # Track usage
                    tool_usage[function_name] = tool_usage.get(function_name, 0) + 1

                    # Log tool usage
                    await tool_ctx.info(f"Agent using tool: {function_name}")

                    # Parse the arguments
                    try:
                        function_args = json.loads(tool_call.function.arguments)
                    except json.JSONDecodeError:
                        function_args = {}

                    # Find the matching tool
                    tool = next((t for t in available_tools if t.name == function_name), None)
                    if not tool:
                        tool_result = f"Error: Tool '{function_name}' not found"
                    # Special handling for clarification requests
                    elif function_name == "request_clarification":
                        try:
                            # Extract clarification parameters
                            request_type = function_args.get("type", "ADDITIONAL_INFO")
                            question = function_args.get("question", "")
                            context = function_args.get("context", {})
                            options = function_args.get("options")

                            # Convert string type to enum
                            clarification_type = ClarificationType[request_type]

                            # Request clarification
                            answer = await self.request_clarification(
                                request_type=clarification_type,
                                question=question,
                                context=context,
                                options=options,
                            )

                            tool_result = self.format_clarification_in_output(question, answer)
                        except Exception as e:
                            tool_result = f"Error processing clarification: {str(e)}"
                    # Special handling for critic requests
                    elif function_name == "critic":
                        try:
                            # Extract critic parameters
                            review_type = function_args.get("review_type", "GENERAL")
                            work_description = function_args.get("work_description", "")
                            code_snippets = function_args.get("code_snippets")
                            file_paths = function_args.get("file_paths")
                            specific_concerns = function_args.get("specific_concerns")

                            # Request critical review
                            tool_result = self.critic_protocol.request_review(
                                review_type=review_type,
                                work_description=work_description,
                                code_snippets=code_snippets,
                                file_paths=file_paths,
                                specific_concerns=specific_concerns,
                            )
                        except Exception as e:
                            tool_result = f"Error processing critic review: {str(e)}"
                    # Special handling for review requests
                    elif function_name == "review":
                        try:
                            # Extract review parameters
                            focus = function_args.get("focus", "GENERAL")
                            work_description = function_args.get("work_description", "")
                            code_snippets = function_args.get("code_snippets")
                            file_paths = function_args.get("file_paths")
                            context = function_args.get("context")

                            # Request balanced review
                            tool_result = self.review_protocol.request_review(
                                focus=focus,
                                work_description=work_description,
                                code_snippets=code_snippets,
                                file_paths=file_paths,
                                context=context,
                            )
                        except Exception as e:
                            tool_result = f"Error processing review: {str(e)}"
                    else:
                        try:
                            tool_result = await tool.call(ctx=tool_ctx.mcp_context, **function_args)
                        except Exception as e:
                            tool_result = f"Error executing {function_name}: {str(e)}"

                    await tool_ctx.info(
                        f"tool {function_name} run with args {function_args} and return {tool_result[: min(100, len(tool_result))]}"
                    )
                    # Add the tool result to the list
                    tool_results_to_add.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": function_name,
                            "content": tool_result,
                        }
                    )

                # Add all tool results to messages atomically
                messages.extend(tool_results_to_add)

                # Log progress
                await tool_ctx.info(f"Processed {len(message.tool_calls)} tool calls. Total: {total_tool_use_count}")

            except Exception as e:
                await tool_ctx.error(f"Error in model call: {str(e)}")
                # Avoid trying to JSON serialize message objects
                await tool_ctx.error(f"Message count: {len(messages)}")

                # CRITICAL FIX: Ensure we add tool_result messages for any tool_use blocks that were added
                # Get the last assistant message (which has the tool_calls)
                last_assistant_msg = None
                for msg in reversed(messages):
                    if msg.get("role") == "assistant" and hasattr(msg, "tool_calls"):
                        last_assistant_msg = msg
                        break

                # If there are orphaned tool calls, add error results for them
                if last_assistant_msg and hasattr(last_assistant_msg, "tool_calls"):
                    # Count how many tool results we already have after this message
                    tool_results_count = 0
                    found_assistant = False
                    for msg in reversed(messages):
                        if msg == last_assistant_msg:
                            found_assistant = True
                            break
                        if found_assistant and msg.get("role") == "tool":
                            tool_results_count += 1

                    # Add error results for any missing tool calls
                    expected_results = len(last_assistant_msg.tool_calls)
                    if tool_results_count < expected_results:
                        for i in range(tool_results_count, expected_results):
                            tool_call = last_assistant_msg.tool_calls[i]
                            messages.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "name": tool_call.function.name,
                                    "content": f"Error: Tool execution interrupted - {str(e)}",
                                }
                            )

                return f"Error in agent execution: {str(e)}"

        # If we've reached the limit, add a warning and get final response
        if total_tool_use_count >= max_tool_uses or iteration_count >= max_iterations:
            messages.append(
                {
                    "role": "system",
                    "content": "You have reached the maximum iteration. Please provide your final response.",
                }
            )

            try:
                # Make a final call to get the result
                final_response = litellm.completion(
                    model=model,
                    messages=messages,
                    temperature=params["temperature"],
                    timeout=params["timeout"],
                    max_tokens=params.get("max_tokens"),
                )

                return (
                    final_response.choices[0].message.content or "Agent reached max iteration limit without a response."
                )  # pyright: ignore
            except Exception as e:
                await tool_ctx.error(f"Error in final model call: {str(e)}")
                return f"Error in final response: {str(e)}"

        # Should not reach here but just in case
        return "Agent execution completed after maximum iterations."

    def _format_result(self, result: str, execution_time: float) -> str:
        """Format agent result with metrics.

        Args:
            result: Raw result from agent
            execution_time: Execution time in seconds

        Returns:
            Formatted result with metrics
        """
        return f"""Agent execution completed in {execution_time:.2f} seconds.

AGENT RESPONSE:
{result}
"""

    @override
    def register(self, mcp_server: FastMCP) -> None:
        """Register this agent tool with the MCP server.

        Creates a wrapper function with explicitly defined parameters that match
        the tool's parameter schema and registers it with the MCP server.

        Args:
            mcp_server: The FastMCP server instance
        """
        tool_self = self  # Create a reference to self for use in the closure

        @mcp_server.tool(name=self.name, description=self.description)
        async def dispatch_agent(prompts: str | list[str], ctx: MCPContext) -> str:
            return await tool_self.call(ctx, prompts=prompts)
