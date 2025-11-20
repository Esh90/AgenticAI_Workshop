# tools/__init__.py
from __future__ import annotations

from pathlib import Path
from typing import List

from crewai.tools import BaseTool

from .calculator import CalculatorTool
from .rag_tool import LocalRAGTool
from .web_search import create_web_search_tool

# --- NEW TOOL IMPORTS ---
from .code_syntax_tool import create_code_syntax_tool, CodeSyntaxTool
from .code_testing_tool import create_code_testing_tool, CodeTestingTool
from .dependency_audit_tool import create_dependency_audit_tool, DependencyAuditTool


__all__ = [
    "create_rag_tool",
    "create_web_search_tool",
    "create_calculator_tool",
    "get_default_toolkit",
    # --- NEW EXPORTS ---
    "create_code_syntax_tool",
    "create_code_testing_tool",
    "create_dependency_audit_tool",
]


DEFAULT_VECTORSTORE_DIR = Path(__file__).resolve().parents[1] / "rag" / "vectorstore"


def create_rag_tool(vectorstore_path: Path | None = None, *, top_k: int = 4) -> LocalRAGTool:
    """Instantiate the local RAG retrieval tool."""
    target_path = vectorstore_path or DEFAULT_VECTORSTORE_DIR
    return LocalRAGTool(vectorstore_path=target_path, top_k=top_k)


def create_calculator_tool() -> CalculatorTool:
    """Instantiate the deterministic calculator tool."""
    # Assuming CalculatorTool is correctly imported from .calculator
    # and has a factory function or is directly instantiated like this.
    return CalculatorTool() 


def get_default_toolkit() -> List[BaseTool]:
    """Provide the standard set of tools shared by research-heavy agents (Planner, Researcher)."""
    return [
        create_rag_tool(),
        create_web_search_tool(),
        create_calculator_tool(),
    ]

# You do not need to add the specialized tools here; they will be explicitly 
# added to the Code Writer, Tester, and Reviewer agents.