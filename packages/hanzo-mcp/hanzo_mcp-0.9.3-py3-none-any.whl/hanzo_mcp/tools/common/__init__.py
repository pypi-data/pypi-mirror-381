"""Common utilities for Hanzo AI tools."""

from mcp.server import FastMCP

from hanzo_mcp.tools.common.base import BaseTool, ToolRegistry
from hanzo_mcp.tools.common.batch_tool import BatchTool
from hanzo_mcp.tools.common.critic_tool import CriticTool
from hanzo_mcp.tools.common.thinking_tool import ThinkingTool


def register_thinking_tool(
    mcp_server: FastMCP,
) -> list[BaseTool]:
    """Register thinking tools with the MCP server.

    Args:
        mcp_server: The FastMCP server instance
    """
    thinking_tool = ThinkingTool()
    ToolRegistry.register_tool(mcp_server, thinking_tool)
    return [thinking_tool]


def register_critic_tool(
    mcp_server: FastMCP,
) -> list[BaseTool]:
    """Register critic tool with the MCP server.

    Args:
        mcp_server: The FastMCP server instance
    """
    critic_tool = CriticTool()
    ToolRegistry.register_tool(mcp_server, critic_tool)
    return [critic_tool]


def register_batch_tool(mcp_server: FastMCP, tools: dict[str, BaseTool]) -> None:
    """Register batch tool with the MCP server.

    Args:
        mcp_server: The FastMCP server instance
        tools: Dictionary mapping tool names to tool instances
    """
    batch_tool = BatchTool(tools)
    ToolRegistry.register_tool(mcp_server, batch_tool)
