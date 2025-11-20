from __future__ import annotations

import logging
from typing import Any

from crewai.tools import BaseTool
from pydantic import Field, PrivateAttr # Added PrivateAttr

# Import the base search tool definition to use its functionality
from .web_search import DuckDuckGoSearchTool, create_web_search_tool

_logger = logging.getLogger(__name__)


class DependencyAuditTool(BaseTool):
    """
    A specialized tool for auditing external libraries for security vulnerabilities 
    and license compliance.
    """

    name: str = "dependency_audit_tool"
    description: str = (
        "Performs a security and compliance check on a list of dependencies. "
        "Provide a comma-separated list of libraries and versions (e.g., 'numpy==1.24.1, requests==2.28.1'). "
        "Use this to find known CVEs or license conflicts."
    )
    
    # FIX: Use PrivateAttr for internal attributes that are not CrewAI tool inputs
    _search_tool: DuckDuckGoSearchTool = PrivateAttr(
        default_factory=lambda: create_web_search_tool(max_results=3),
    )

    def _run(self, dependency_list: str) -> str:
        results = []
        dependencies = [dep.strip() for dep in dependency_list.split(',') if dep.strip()]
        
        if not dependencies:
            return "No dependencies provided for audit."

        # Audit each dependency with a focused query
        for dep in dependencies:
            focused_query = f"security vulnerability and license for {dep}"
            _logger.info("DependencyAuditTool executing search for: %s", dep)
            
            # Use the underlying search tool
            # Access the private attribute using dot notation
            search_results = self._search_tool._run(focused_query)
            results.append(f"Audit Results for **{dep}**:\n{search_results}")
            
        return "--- Dependency Audit Report ---\n\n" + "\n\n".join(results)


def create_dependency_audit_tool() -> DependencyAuditTool:
    """Instantiate the specialized Dependency Audit tool."""
    return DependencyAuditTool()