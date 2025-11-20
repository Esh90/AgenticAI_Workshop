from __future__ import annotations

import logging
from typing import Any

from crewai.tools import BaseTool
from pydantic import Field, PrivateAttr # Added PrivateAttr

# Import the base search tool definition to use its functionality
from .web_search import DuckDuckGoSearchTool, create_web_search_tool

_logger = logging.getLogger(__name__)


class CodeTestingTool(BaseTool):
    """
    A specialized search tool for finding testing frameworks, test case patterns, 
    and common bug/vulnerability types.
    """

    name: str = "testing_framework_tool"
    description: str = (
        "Search for testing frameworks (pytest, Jest, JUnit), test patterns, "
        "mocking guides, and common bug/security vulnerability types for a given context. "
        "Provide a concise query about testing concepts or known vulnerabilities."
    )
    
    # FIX: Use PrivateAttr for internal attributes that are not CrewAI tool inputs
    _search_tool: DuckDuckGoSearchTool = PrivateAttr(
        default_factory=lambda: create_web_search_tool(max_results=3),
    )

    def _run(self, query: str) -> str:
        # Prepend context to the query for better, testing-focused results
        focused_query = f"testing framework {query} test case example vulnerability"
        _logger.info("CodeTestingTool executing focused search: %s", focused_query)

        # Execute the search using the underlying DuckDuckGo tool
        # Access the private attribute using dot notation
        search_results = self._search_tool._run(focused_query)
        
        # Add a helpful header to the results
        return f"--- Testing Tool Results for '{query}' ---\n\n{search_results}"


def create_code_testing_tool() -> CodeTestingTool:
    """Instantiate the specialized Code Testing Search tool."""
    return CodeTestingTool()