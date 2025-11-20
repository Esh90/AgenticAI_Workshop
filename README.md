# Code Development Assistant: Multi-Agent System

A hands-on project template that demonstrates how to orchestrate specialized CrewAI agents for end-to-end software development workflows: Planning, Writing, Testing, and Code Review.

The stack combines CrewAI with specialized LangChain tools, a FAISS-backed Retrieval-Augmented Generation (RAG) pipeline, and a Streamlit frontend. All large language model calls are routed through the OpenRouter API using the stable and fast model: `mistralai/mistral-7b-instruct`.

---

## 1. Project Goals and Architecture

The primary goal of this project is to showcase a robust, fully automated, and self-correcting software development cycle using collaborative AI agents.

### Key Architecture Showcase

- **Multi-Agent Orchestration (CrewAI):** Structuring four specialized agents in a strictly sequential pipeline where output from one task (e.g., the Plan) becomes the context for the next (the Code).

- **RAG for Standards:** Illustrating how the RAG pipeline augments agents with internal, curated context (coding standards, security guides) via FAISS, ensuring adherence to internal best practices.

- **Specialized Tooling:** Implementing custom tools that provide targeted capabilities, moving beyond basic web search for critical tasks like code syntax checking and dependency auditing.

- **Performance and Stability:** Using the high-throughput `mistralai/mistral-7b-instruct` model to maintain fast execution speeds suitable for deployment.

---

## 2. Project Structure

The structure is designed for clear separation of concerns, mapping directly to the CrewAI framework and auxiliary services:

```
code-dev-assistant/
├── .env.example
├── requirements.txt
├── README.md                 <-- This file
├── main.py                   <-- CLI entrypoint
├── crew.py                   <-- Crew and Agent Orchestration logic
├── tasks.py                  <-- Defines the 4 sequential tasks
│
├── config/
│   ├── settings.py           <-- LLM/Model Configuration (Swapped to Mistral)
│   └── logging_config.py
│
├── agents/
│   ├── __init__.py           <-- Exports the agent creation helpers
│   ├── code_planner.py       <-- Role: Architect, Max Iterations: 8 (Optimized for speed)
│   ├── code_writer.py        <-- Role: Senior Engineer, uses Syntax Tool
│   ├── code_tester.py        <-- Role: QA Engineer, uses Testing Tool
│   └── code_reviewer.py      <-- Role: Security Auditor, uses Audit Tool
│
├── tools/
│   ├── __init__.py           <-- Registers all 6 tools
│   ├── rag_tool.py           <-- FAISS Retrieval Tool
│   ├── web_search.py         <-- General Web Search (Stabilized with DDGS fixes)
│   ├── calculator.py         <-- Deterministic Calculator
│   ├── code_syntax_tool.py   <-- NEW: Specialized tool for code formatting/syntax
│   ├── code_testing_tool.py  <-- NEW: Specialized tool for testing frameworks/patterns
│   └── dependency_audit_tool.py <-- NEW: Specialized tool for security/dependency checks
│
├── rag/
│   ├── build_vector_db.py
│   └── documents/
│       ├── coding_best_practices.txt
│       ├── design_patterns.txt
│       ├── error_handling.txt
│       ├── testing_frameworks.txt
│       └── security_best_practices.txt <-- NEW: Added security context for Reviewer/Tester
│
└── frontend/
   └── app.py                 <-- Streamlit web interface
```

---

## 3. Built-in Agent Tooling

Every agent in the crew has access to a toolkit tailored to their function.

| Tool Name                     | Type     | Purpose                                                                 | Primary User(s)            |
|-------------------------------|----------|-------------------------------------------------------------------------|-----------------------------|
| `local_rag_search`            | Custom   | RAG over internal documents for coding standards and security best practices. | All                         |
| `duckduckgo_search`          | Standard | Live web search for general questions or external documentation lookups. | All                         |
| `deterministic_calculator`    | Standard | Quick, reliable math for complexity estimates or test assertions.         | Planner, Tester, Reviewer   |
| `code_syntax_tool`            | Custom   | Focused lookup for specific language syntax and best practices (e.g., Python list comprehension). | Code Writer                 |
| `testing_framework_tool`      | Custom   | Searches for framework-specific test case patterns (e.g., pytest fixtures, Jest mocks). | Code Tester                 |
| `dependency_audit_tool`      | Custom   | Checks external libraries for security vulnerabilities (CVEs) and license compliance. | Code Reviewer                |

---

## 4. Installation and Setup

### Prerequisites

- Python 3.10+
- An OpenRouter account and API key (set in .env file)
- A virtual environment manager (venv recommended)

### Step-by-Step Setup

1. Clone the repository (if applicable) and navigate to the directory.

2. Create and activate a virtual environment

    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\Activate.ps1
    # macOS/Linux
    source .venv/bin/activate
    ```

3. Install project dependencies

    ```bash
    pip install -r requirements.txt
    # Ensure the modern DuckDuckGo library is installed:
    pip install ddgs
    ```

4. Set up environment variables

    ```bash
    copy .env.example .env
    # Edit .env and paste your actual OpenRouter API key:
    # OPENROUTER_API_KEY=your_key_here
    ```

5. Build the FAISS vector store (one-time setup)

    The RAG system is updated with documents on security and best practices. This step builds the index from the documents in `rag/documents/`.

    ```bash
    python rag\build_vector_db.py
    ```

---

## 5. Running the Pipeline

### Command Line Interface (Fast Execution)

Execute the crew directly from the command line, providing a specific coding task.

```bash
python main.py --topic "Develop a secure Python function to sanitize user input for SQL injection."
```

### Streamlit Frontend (Visual Demo)

Launch the interactive UI to run the pipeline visually:

```bash
python -m streamlit run frontend\app.py
```

Access at: [http://localhost:8501](http://localhost:8501)

---

## 6. Optimization Summary

To resolve the initial Rate Limit errors (Error 429) and excessive run times, the following optimizations were implemented:

- **LLM Model Swap:** The default model in `config/settings.py` was changed from the slow, rate-limited `meta-llama/llama-3.3-70b-instruct:free` to the fast, high-throughput `mistralai/mistral-7b-instruct`.

- **Planner Optimization:** The `max_iter` for the Code Planner agent was reduced from 15 to 8 to force faster decision-making, cutting down the total time spent in the critical planning stage.

- **Tool Stability:** The `tools/web_search.py` file was refactored to use the modern `ddgs` library and with statements, eliminating ResourceWarning and improving stability for continuous deployment.

This robust configuration ensures a reliable and responsive demonstration of the four-stage Code Development Assistant workflow.

---

## 7. Team & Contribution Summary

This project was developed through a collaborative effort. The table below outlines the primary responsibilities and core deliverables owned by each team member:

| Team Member    | Agent Role(s)                        | Core Technical Contributions (Ownership)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You (Lead)     | Code Tester, Code Reviewer + Orchestrator | Lead Architecture & Flow: Defined project flow, managed end-to-end integration (`crew.py`, `main.py`), set up LLM configuration and tuning. Quality & Infrastructure: Developed Code Tester/Reviewer agents, built the RAG Pipeline, created the `web_search.py` utility and the `dependency_audit_tool.py`. Presentation Layer: Engineered the custom Streamlit Dashboard (`frontend/app.py`).                                                                                                                                                                                                                     |
| Alveena Khan   | Code Planner                         | Planning & Core Tooling: Developed the Code Planner agent (architecture design), performed Planner LLM optimization (`max_iter` reduction), and created and integrated the `code_syntax_tool.py` utility.                                                                                                                                                                                                                                                                                                                                                       |
| Eiman Fatima   | Code Writer                         | Implementation & Test Tooling: Developed the Code Writer agent (responsible for generating the actual code output), and created and integrated the specialized quality tool `code_testing_tool.py`.                                                                                                                                                                                                                                                                                                                                                       |

This robust attribution section clearly delineates your team's contributions for formal evaluation.