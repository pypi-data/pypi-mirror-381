"""Vector search tool for semantic document retrieval."""

import json
from typing import List, Unpack, Optional, TypedDict, final

from mcp.server.fastmcp import Context as MCPContext

from hanzo_mcp.tools.common.auto_timeout import auto_timeout

from hanzo_mcp.tools.common.base import BaseTool
from hanzo_mcp.tools.common.permissions import PermissionManager

from .project_manager import ProjectVectorManager


class VectorSearchParams(TypedDict, total=False):
    """Parameters for vector search operations."""

    query: str
    limit: Optional[int]
    score_threshold: Optional[float]
    include_content: Optional[bool]
    file_filter: Optional[str]
    project_filter: Optional[List[str]]
    search_scope: Optional[str]  # "all", "global", "current", or specific project name


@final
class VectorSearchTool(BaseTool):
    """Tool for semantic search in the vector database."""

    def __init__(
        self,
        permission_manager: PermissionManager,
        project_manager: ProjectVectorManager,
    ):
        """Initialize the vector search tool.

        Args:
            permission_manager: Permission manager for access control
            project_manager: Project-aware vector store manager
        """
        self.permission_manager = permission_manager
        self.project_manager = project_manager

    @property
    def name(self) -> str:
        """Get the tool name."""
        return "vector_search"

    @property
    def description(self) -> str:
        """Get the tool description."""
        return """Pure semantic/vector search using Infinity embedded database.

Searches indexed documents using vector embeddings to find semantically similar content.
This is NOT keyword search - it finds documents based on meaning and context similarity.

Features:
- Searches across project-specific vector databases
- Returns similarity scores (0-1, higher is better)
- Supports filtering by project or file
- Automatically detects projects via LLM.md files

Use 'grep' for exact text/pattern matching, 'vector_search' for semantic similarity."""

    @auto_timeout("vector_search")


    async def call(
        self,
        ctx: MCPContext,
        **params: Unpack[VectorSearchParams],
    ) -> str:
        """Search for similar documents in the vector database.

        Args:
            ctx: MCP context
            **params: Tool parameters

        Returns:
            Search results formatted as text
        """
        query = params.get("query")
        if not query:
            return "Error: query parameter is required"

        limit = params.get("limit", 10)
        score_threshold = params.get("score_threshold", 0.0)
        include_content = params.get("include_content", True)
        file_filter = params.get("file_filter")
        project_filter = params.get("project_filter")
        search_scope = params.get("search_scope", "all")

        try:
            # Determine search strategy based on scope
            if search_scope == "all":
                # Search across all projects
                project_results = await self.project_manager.search_all_projects(
                    query=query,
                    limit_per_project=limit,
                    score_threshold=score_threshold,
                    include_global=True,
                    project_filter=project_filter,
                )

                # Combine and sort all results
                all_results = []
                for project_name, results in project_results.items():
                    for result in results:
                        # Add project info to metadata
                        result.document.metadata = result.document.metadata or {}
                        result.document.metadata["search_project"] = project_name
                        all_results.append(result)

                # Sort by score and limit
                all_results.sort(key=lambda x: x.score, reverse=True)
                results = all_results[:limit]

            elif search_scope == "global":
                # Search only global store
                global_store = self.project_manager._get_global_store()
                results = global_store.search(
                    query=query,
                    limit=limit,
                    score_threshold=score_threshold,
                )
                for result in results:
                    result.document.metadata = result.document.metadata or {}
                    result.document.metadata["search_project"] = "global"

            else:
                # Search specific project or current context
                if search_scope != "current":
                    # Search specific project by name
                    project_info = None
                    for _proj_key, proj_info in self.project_manager.projects.items():
                        if proj_info.name == search_scope:
                            project_info = proj_info
                            break

                    if project_info:
                        vector_store = self.project_manager.get_vector_store(project_info)
                        results = vector_store.search(
                            query=query,
                            limit=limit,
                            score_threshold=score_threshold,
                        )
                        for result in results:
                            result.document.metadata = result.document.metadata or {}
                            result.document.metadata["search_project"] = project_info.name
                    else:
                        return f"Project '{search_scope}' not found"
                else:
                    # For "current", try to detect from working directory
                    import os

                    current_dir = os.getcwd()
                    project_info = self.project_manager.get_project_for_path(current_dir)

                    if project_info:
                        vector_store = self.project_manager.get_vector_store(project_info)
                        results = vector_store.search(
                            query=query,
                            limit=limit,
                            score_threshold=score_threshold,
                        )
                        for result in results:
                            result.document.metadata = result.document.metadata or {}
                            result.document.metadata["search_project"] = project_info.name
                    else:
                        # Fall back to global store
                        global_store = self.project_manager._get_global_store()
                        results = global_store.search(
                            query=query,
                            limit=limit,
                            score_threshold=score_threshold,
                        )
                        for result in results:
                            result.document.metadata = result.document.metadata or {}
                            result.document.metadata["search_project"] = "global"

            if not results:
                return f"No results found for query: '{query}'"

            # Filter by file if requested
            if file_filter:
                results = [r for r in results if file_filter in (r.document.file_path or "")]

            # Format results
            output_lines = [f"Found {len(results)} results for query: '{query}'\n"]

            for i, result in enumerate(results, 1):
                doc = result.document
                score_percent = result.score * 100

                # Header with score and metadata
                project_name = doc.metadata.get("search_project", "unknown")
                header = f"Result {i} (Score: {score_percent:.1f}%) - Project: {project_name}"
                if doc.file_path:
                    header += f" - {doc.file_path}"
                    if doc.chunk_index is not None:
                        header += f" [Chunk {doc.chunk_index}]"

                output_lines.append(header)
                output_lines.append("-" * len(header))

                # Add metadata if available
                if doc.metadata:
                    relevant_metadata = {
                        k: v
                        for k, v in doc.metadata.items()
                        if k not in ["chunk_number", "total_chunks", "search_project"]
                    }
                    if relevant_metadata:
                        output_lines.append(f"Metadata: {json.dumps(relevant_metadata, indent=2)}")

                # Add content if requested
                if include_content:
                    content = doc.content
                    if len(content) > 500:
                        content = content[:500] + "..."
                    output_lines.append(f"Content:\n{content}")

                output_lines.append("")  # Empty line between results

            return "\n".join(output_lines)

        except Exception as e:
            return f"Error searching vector database: {str(e)}"

    def register(self, mcp_server) -> None:
        """Register this tool with the MCP server.

        Args:
            mcp_server: The FastMCP server instance
        """
        # This is a placeholder - the actual registration would happen
        # through the MCP server's tool registration mechanism
        pass
