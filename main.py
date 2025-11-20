"""Entrypoint for running the Agentic AI Code Development Assistant pipeline end-to-end."""
from __future__ import annotations

import argparse
import logging

from dotenv import load_dotenv

from crew import run_code_development_pipeline # Renamed Import
from config.logging_config import configure_logging


def run_pipeline(topic: str) -> str:
    """Run the configured crew against the provided coding task topic."""
    load_dotenv()
    configure_logging()
    logging.getLogger(__name__).info("Starting Code Development pipeline for topic: %s", topic)
    return run_code_development_pipeline(topic) # Renamed Function Call


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Agentic AI Code Development Assistant crew pipeline.")
    parser.add_argument(
        "--topic",
        # Updated default topic to a coding task instead of a workshop theme
        default="Create a Python function to check if a string is a palindrome.", 
        help="The coding task to guide the crew's planning and implementation.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    output = run_pipeline(args.topic)
    print(output)