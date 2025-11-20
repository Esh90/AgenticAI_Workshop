#"""Crew assembly for the Agentic AI Code Development Assistant."""
from __future__ import annotations

import logging
from typing import Any

from crewai import Crew, Process

# Import the helper function to get all agents
from agents import get_all_code_agents

from config.settings import OpenRouterLLMConfig
from tasks import build_code_tasks # Using the corrected tasks function
from tools import (
    get_default_toolkit,
    create_code_syntax_tool,
    create_code_testing_tool,
    create_dependency_audit_tool,
)

logger = logging.getLogger(__name__)


def create_code_development_crew(llm_overrides: dict[str, Any] | None = None) -> Crew:
    """Instantiate the Code Development Assistant crew with specialized agents and tools."""
    
    # 1. Define common and specialized toolkits
    default_tools = get_default_toolkit()  # RAG, Web Search, Calculator

    planner_tools = default_tools
    writer_tools = default_tools + [create_code_syntax_tool()]
    tester_tools = default_tools + [create_code_testing_tool()]
    reviewer_tools = default_tools + [create_dependency_audit_tool()]

    # 2. Instantiate all Code Agents using the helper function
    code_agents = get_all_code_agents(
        planner_tools=planner_tools,
        writer_tools=writer_tools,
        tester_tools=tester_tools,
        reviewer_tools=reviewer_tools,
        llm_overrides=llm_overrides
    )
    
    # Extract agents from the dictionary
    code_planner = code_agents['planner']
    code_writer = code_agents['writer']
    code_tester = code_agents['tester']
    code_reviewer = code_agents['reviewer']

    # 3. Define Tasks (using the correct build_code_tasks function)
    # NOTE: The build_code_tasks function takes care of assigning the correct tools
    # to the *tasks* as well, ensuring tools are available during execution.
    tasks = build_code_tasks(
        code_planner=code_planner,
        code_writer=code_writer,
        code_tester=code_tester,
        code_reviewer=code_reviewer,
    )
    
    # 4. Instantiate Crew
    return Crew(
        agents=[code_planner, code_writer, code_tester, code_reviewer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )


# The helper functions below (_build_llm_attempts, _sanitize_overrides, _execute_crew)
# remain largely the same, but we will slightly rename the main runner function 
# to reflect the new project focus.

def _build_llm_attempts(config: OpenRouterLLMConfig) -> list[dict[str, Any]]:
    """Construct an ordered list of LLM override attempts from config."""

    attempts: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    base_urls = [config.base_url, *config.fallback_base_urls]
    models = [config.model, *config.fallback_models]

    base_urls = list(dict.fromkeys(base_urls))
    models = list(dict.fromkeys(models))

    for provider in ("openrouter", "openai"):
        for model in models:
            for base_url in base_urls:
                key = (provider, model, base_url)
                if key in seen:
                    continue
                seen.add(key)

                override: dict[str, Any] = {}

                if base_url != config.base_url:
                    override["base_url"] = base_url

                if provider == "openrouter":
                    if model != config.model:
                        override["model"] = model
                else:
                    override["provider"] = "openai"
                    override["model"] = model
                    if config.headers:
                        override["default_headers"] = dict(config.headers)
                        override["extra_headers"] = dict(config.headers)

                attempts.append(override)

    if not attempts:
        attempts.append({})

    return attempts


def _sanitize_overrides(overrides: dict[str, Any]) -> dict[str, Any]:
    """Remove verbose or sensitive values before logging overrides."""

    sanitized = dict(overrides)
    for key in ("extra_headers", "default_headers", "api_key"):
        if key in sanitized:
            sanitized[key] = "[set]"
    return sanitized


def _execute_crew(
    topic: str, overrides: dict[str, Any], config: OpenRouterLLMConfig
) -> str:
    # Changed to use the new code development crew factory
    crew = create_code_development_crew(llm_overrides=overrides) 
    provider_label = overrides.get("provider", "openrouter-liteLLM")
    model_label = overrides.get("model", config.model)
    base_url_label = overrides.get("base_url", config.base_url)
    logger.info(
        "Code Development Crew kickoff started for topic: %s (provider=%s model=%s base_url=%s)",
        topic,
        provider_label,
        model_label,
        base_url_label,
    )
    # The topic input is passed directly to the kickoff call
    result = crew.kickoff(inputs={"topic": topic}) 

    for task in crew.tasks:
        task_output = getattr(task, "output", None)
        if task_output:
            logger.info("Task '%s' output:\n%s", task.name, task_output)

    if isinstance(result, str):
        logger.info("Crew completed with final output length=%d characters", len(result))
        return result

    candidate = getattr(result, "raw_output", None) or getattr(result, "output", None)
    if candidate:
        output_text = str(candidate)
        logger.info("Crew completed with final output length=%d characters", len(output_text))
        return output_text

    output_text = str(result)
    logger.info("Crew completed with final output length=%d characters", len(output_text))
    return output_text


def run_code_development_pipeline(topic: str) -> str:
    """Run the code development crew for a given task topic with OpenRouter fallback attempts."""

    config = OpenRouterLLMConfig()
    attempts = _build_llm_attempts(config)

    last_error: Exception | None = None
    total_attempts = len(attempts)

    for index, overrides in enumerate(attempts, start=1):
        try:
            if overrides:
                logger.info(
                    "Attempt %d/%d using overrides: %s",
                    index,
                    total_attempts,
                    _sanitize_overrides(overrides),
                )
            result = _execute_crew(topic, overrides, config)
            if index > 1:
                logger.info(
                    "Fallback succeeded on attempt %d/%d with overrides: %s",
                    index,
                    total_attempts,
                    _sanitize_overrides(overrides),
                )
            return result
        except Exception as exc:  # pragma: no cover - runtime resilience path
            last_error = exc
            logger.exception(
                "Crew run failed on attempt %d/%d with overrides %s",
                index,
                total_attempts,
                _sanitize_overrides(overrides),
            )

    assert last_error is not None  # defensive: should be set if all attempts failed
    raise last_error