"""Base classes for Hanzo AI tools.

This module provides abstract base classes that define interfaces and common functionality
for all tools used in Hanzo AI. These abstractions help ensure consistent tool
behavior and provide a foundation for tool registration and management.
"""

import functools
from abc import ABC, abstractmethod
from typing import Any, Callable, final
from collections.abc import Awaitable

from mcp.server import FastMCP

from hanzo_mcp.tools.common.auto_timeout import auto_timeout
from mcp.server.fastmcp import Context as MCPContext

from hanzo_mcp.tools.common.validation import (
    ValidationResult,
    validate_path_parameter,
)
from hanzo_mcp.tools.common.permissions import PermissionManager


def handle_connection_errors(
    func: Callable[..., Awaitable[str]],
) -> Callable[..., Awaitable[str]]:
    """Decorator to handle connection errors in MCP tool functions.

    This decorator wraps tool functions to catch ClosedResourceError and other
    connection-related exceptions that occur when the client disconnects.

    Args:
        func: The async tool function to wrap

    Returns:
        Wrapped function that handles connection errors gracefully
    """

    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> str:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            # Check if this is a connection-related error
            error_name = type(e).__name__
            if any(
                name in error_name
                for name in [
                    "ClosedResourceError",
                    "ConnectionError",
                    "BrokenPipeError",
                ]
            ):
                # Client has disconnected - log the error but don't crash
                # Return a simple error message (though it likely won't be received)
                return f"Client disconnected during operation: {error_name}"
            else:
                # Re-raise non-connection errors
                raise

    return wrapper


class BaseTool(ABC):
    """Abstract base class for all Hanzo AI tools.

    This class defines the core interface that all tools must implement, ensuring
    consistency in how tools are registered, documented, and called.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the tool name.

        Returns:
            The tool name as it will appear in the MCP server
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Get the tool description.

        Returns:
            Detailed description of the tool's purpose and usage
        """
        pass

    @abstractmethod
    @auto_timeout("base")

    async def call(self, ctx: MCPContext, **params: Any) -> Any:
        """Execute the tool with the given parameters.

        Args:
            ctx: MCP context for the tool call
            **params: Tool parameters provided by the caller

        Returns:
            Tool execution result as a string
        """
        pass

    @abstractmethod
    def register(self, mcp_server: FastMCP) -> None:
        """Register this tool with the MCP server.

        This method must be implemented by each tool class to create a wrapper function
        with explicitly defined parameters that calls this tool's call method.
        The wrapper function is then registered with the MCP server.

        Args:
            mcp_server: The FastMCP server instance
        """
        pass


class FileSystemTool(BaseTool, ABC):
    """Base class for filesystem-related tools.

    Provides common functionality for working with files and directories,
    including permission checking and path validation.
    """

    def __init__(self, permission_manager: PermissionManager) -> None:
        """Initialize filesystem tool.

        Args:
            permission_manager: Permission manager for access control
        """
        self.permission_manager: PermissionManager = permission_manager

    def validate_path(self, path: str, param_name: str = "path") -> ValidationResult:
        """Validate a path parameter.

        Args:
            path: Path to validate
            param_name: Name of the parameter (for error messages)

        Returns:
            Validation result containing validation status and error message if any
        """
        return validate_path_parameter(path, param_name)

    def is_path_allowed(self, path: str) -> bool:
        """Check if a path is allowed according to permission settings.

        Args:
            path: Path to check

        Returns:
            True if the path is allowed, False otherwise
        """
        return self.permission_manager.is_path_allowed(path)


@final
class ToolRegistry:
    """Registry for Hanzo AI tools.

    Provides functionality for registering tool implementations with an MCP server,
    handling the conversion between tool classes and MCP tool functions.
    """

    @staticmethod
    def register_tool(mcp_server: FastMCP, tool: BaseTool) -> None:
        """Register a tool with the MCP server.

        Args:
            mcp_server: The FastMCP server instance
            tool: The tool to register
        """
        # Check if tool is enabled before registering
        # Import here to avoid circular imports
        from hanzo_mcp.tools.common.tool_enable import ToolEnableTool

        if ToolEnableTool.is_tool_enabled(tool.name):
            # Use the tool's register method which handles all the details
            tool.register(mcp_server)

    @staticmethod
    def register_tools(mcp_server: FastMCP, tools: list[BaseTool]) -> None:
        """Register multiple tools with the MCP server.

        Args:
            mcp_server: The FastMCP server instance
            tools: List of tools to register
        """
        for tool in tools:
            ToolRegistry.register_tool(mcp_server, tool)
