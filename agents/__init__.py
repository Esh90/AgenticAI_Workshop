"""
Exports agent creation functions and the convenience function 
to build all code development agents.
"""
from __future__ import annotations

from typing import Any, Iterable, Optional

# Import the new, renamed agent creation functions
from .code_planner import create_code_planner_agent
from .code_writer import create_code_writer_agent
from .code_tester import create_code_tester_agent
from .code_reviewer import create_code_reviewer_agent

# Use __all__ to define what gets exposed when importing * from agents
__all__ = [
    "create_code_planner_agent",
    "create_code_writer_agent",
    "create_code_tester_agent",
    "create_code_reviewer_agent",
    "get_all_code_agents",
]


def get_all_code_agents(
    planner_tools: Optional[Iterable[object]] = None,
    writer_tools: Optional[Iterable[object]] = None,
    tester_tools: Optional[Iterable[object]] = None,
    reviewer_tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> dict:
    """
    Convenience function to create all code development agents at once.
    
    Returns:
        dict: Dictionary with keys 'planner', 'writer', 'tester', 'reviewer'
    """
    return {
        'planner': create_code_planner_agent(tools=planner_tools, llm_overrides=llm_overrides),
        'writer': create_code_writer_agent(tools=writer_tools, llm_overrides=llm_overrides),
        'tester': create_code_tester_agent(tools=tester_tools, llm_overrides=llm_overrides),
        'reviewer': create_code_reviewer_agent(tools=reviewer_tools, llm_overrides=llm_overrides),
    }