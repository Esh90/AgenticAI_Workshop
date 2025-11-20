from __future__ import annotations

import logging
from typing import Any

from crewai.tools import BaseTool
from pydantic import Field, PrivateAttr # Added PrivateAttr

# Import the base search tool definition to use its functionality
from .web_search import DuckDuckGoSearchTool, create_web_search_tool

_logger = logging.getLogger(__name__)


class CodeSyntaxTool(BaseTool):
    """
    A specialized search tool for finding correct syntax, code patterns, and best practices.
    It wraps the DuckDuckGo search to be more focused on code-related queries.
    """

    name: str = "code_syntax_tool"
    description: str = (
        "Search for correct language syntax, standard library usage, code patterns, "
        "and language-specific best practices (e.g., Python, JavaScript, Java). "
        "Provide a concise search phrase focused on code elements."
    )
    
    # FIX: Use PrivateAttr for internal attributes that are not CrewAI tool inputs
    _search_tool: DuckDuckGoSearchTool = PrivateAttr(
        default_factory=lambda: create_web_search_tool(max_results=3),
    )

    def _run(self, query: str) -> str:
        # Prepend context to the query for better, code-focused results
        focused_query = f"{query} code syntax example best practice"
        _logger.info("CodeSyntaxTool executing focused search: %s", focused_query)

        # Execute the search using the underlying DuckDuckGo tool
        # Access the private attribute using dot notation
        search_results = self._search_tool._run(focused_query)
        
        # Add a helpful header to the results
        return f"--- Code Syntax Tool Results for '{query}' ---\n\n{search_results}"


def create_code_syntax_tool() -> CodeSyntaxTool:
    """Instantiate the specialized Code Syntax Search tool."""
    return CodeSyntaxTool()