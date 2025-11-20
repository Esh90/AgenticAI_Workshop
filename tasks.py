"""Task definitions for the Agentic AI Workshop crew."""
from __future__ import annotations

from typing import List

from crewai import Task

from tools import (
    create_calculator_tool, 
    create_rag_tool, 
    create_web_search_tool,
    # --- NEW TOOL IMPORTS ---
    create_code_syntax_tool,
    create_code_testing_tool,
    create_dependency_audit_tool,
)


# ============================================================================
# WORKSHOP CONTENT TASKS (These tasks remain unchanged, using default tools)
# ============================================================================

def create_planning_task(agent) -> Task:
    """Create a comprehensive execution plan for the workshop."""
    # ... (content remains the same)
    return Task(
        description=(
            "Analyze the workshop topic '{topic}' and craft a detailed, milestone-based execution plan. "
            "Your plan should include:\n"
            "1. Clear learning objectives and target audience definition\n"
            "2. Three to five major milestones with specific deliverables\n"
            "3. Required resources (tools, libraries, datasets, documentation)\n"
            "4. Role assignments and responsibilities for each phase\n"
            "5. Realistic timeline with buffer periods\n"
            "6. Potential risks and mitigation strategies\n"
            "7. Success metrics and evaluation criteria\n\n"
            "Ensure the plan is actionable, measurable, and aligned with best practices "
            "for technical workshop development."
        ),
        expected_output=(
            "A structured execution plan document containing:\n"
            "- Executive summary with key objectives\n"
            "- Detailed milestone breakdown with timelines\n"
            "- Resource requirements matrix\n"
            "- Risk assessment table\n"
            "- Success criteria and KPIs\n"
            "- Dependencies and critical path analysis"
        ),
        agent=agent,
        name="Planning",
    )


def create_research_task(agent, tools=None) -> Task:
    """Gather and validate supporting research from multiple sources."""
    tools = list(tools) if tools is not None else [
        create_rag_tool(),
        create_web_search_tool(),
        create_calculator_tool(),
    ]
    # ... (rest of function body remains the same)
    return Task(
        description=(
            "Conduct comprehensive research to validate and enrich the execution plan for '{topic}'. "
            "Your research should:\n"
            "1. Use the RAG tool to query the local knowledge base for relevant documentation\n"
            "2. Perform web searches to find current best practices, tutorials, and case studies\n"
            "3. Identify at least 5 trustworthy sources (official docs, research papers, reputable blogs)\n"
            "4. Gather data points, statistics, and benchmarks that justify each milestone\n"
            "5. Use the calculator tool to validate any numerical claims or projections\n"
            "6. Document common pitfalls and lessons learned from similar workshops\n"
            "7. Identify prerequisite knowledge and skill gaps to address\n\n"
            "Cite all sources with inline references and maintain academic rigor in your findings."
        ),
        expected_output=(
            "A comprehensive research report including:\n"
            "- Executive summary of key findings\n"
            "- Annotated bibliography with at least 5 authoritative sources\n"
            "- Data-driven insights supporting each milestone\n"
            "- RAG document references and relevant excerpts\n"
            "- Validated statistics and calculations\n"
            "- Best practices and common pitfalls analysis\n"
            "- Gap analysis and prerequisite recommendations"
        ),
        agent=agent,
        tools=tools,
        name="Research",
    )


def create_writing_task(agent) -> Task:
    """Author comprehensive workshop deliverables."""
    # ... (content remains the same)
    return Task(
        description=(
            "Draft a complete, professional workshop guide for '{topic}' that synthesizes "
            "the planning and research outputs. Your guide should include:\n"
            "1. Engaging introduction with clear learning objectives\n"
            "2. Target audience and prerequisites section\n"
            "3. Workshop agenda with time allocations\n"
            "4. Step-by-step hands-on labs with code examples\n"
            "5. Deployment and setup instructions\n"
            "6. Troubleshooting guide and FAQs\n"
            "7. Additional resources and next steps\n"
            "8. Assessment criteria or quiz questions\n\n"
            "Incorporate research insights, statistical evidence, and practical examples throughout. "
            "Use clear, accessible language suitable for the target audience. "
            "Format all code blocks properly and ensure reproducibility."
        ),
        expected_output=(
            "A complete Markdown-formatted workshop guide with:\n"
            "- Table of contents with anchor links\n"
            "- Workshop overview and objectives\n"
            "- Prerequisites and environment setup\n"
            "- Detailed agenda with time blocks\n"
            "- 3-5 hands-on lab exercises with code\n"
            "- Deployment instructions and configuration examples\n"
            "- Troubleshooting section\n"
            "- Resources, references, and further reading\n"
            "- Optional assessment questions"
        ),
        agent=agent,
        name="Writing",
    )


def create_review_task(agent) -> Task:
    """Review and provide feedback on workshop deliverables."""
    # ... (content remains the same)
    return Task(
        description=(
            "Conduct a thorough review of the workshop content for '{topic}' and provide "
            "actionable feedback. Evaluate the following dimensions:\n"
            "1. **Accuracy**: Verify technical correctness and validity of all claims\n"
            "2. **Completeness**: Ensure all promised content is delivered\n"
            "3. **Pedagogy**: Assess learning flow, clarity, and engagement\n"
            "4. **Practicality**: Confirm labs are reproducible and relevant\n"
            "5. **Accessibility**: Check if prerequisites and explanations are appropriate\n"
            "6. **Consistency**: Verify formatting, terminology, and style alignment\n\n"
            "Provide specific, constructive feedback with line references where applicable. "
            "Categorize issues by severity (critical, major, minor) and offer concrete solutions."
        ),
        expected_output=(
            "A comprehensive review report containing:\n"
            "- Executive summary with overall assessment\n"
            "- Strengths and highlights section\n"
            "- Critical issues requiring immediate attention\n"
            "- Major improvements with specific recommendations\n"
            "- Minor suggestions and polish items\n"
            "- Final recommendation (Approve / Revise / Reject)\n"
            "- Estimated effort for implementing changes"
        ),
        agent=agent,
        name="Reviewing",
    )

# ---

# ============================================================================
# CODE DEVELOPMENT TASKS (These tasks are updated to include the new tools)
# ============================================================================

def create_code_planning_task(agent) -> Task:
    """Plan the software architecture and implementation approach."""
    # Code Planner uses the default toolkit (RAG, Web Search, Calculator) 
    # which is passed in the build_code_tasks function via code_tools.
    return Task(
        description=(
            "Design a comprehensive software architecture plan for '{topic}'. Your plan should include:\n"
            "1. **Requirements Analysis**: Break down functional and non-functional requirements\n"
            "2. **Architecture Design**: Define system components, modules, and their interactions\n"
            "3. **Technology Stack**: Select appropriate languages, frameworks, libraries, and tools\n"
            "4. **Data Models**: Design database schemas, data structures, and APIs\n"
            "5. **Code Organization**: Define directory structure, naming conventions, and module boundaries\n"
            "6. **Development Milestones**: Break implementation into logical, testable phases\n"
            "7. **Quality Standards**: Define coding standards, documentation requirements, and testing criteria\n"
            "8. **Dependencies**: Identify external libraries and version constraints\n"
            "9. **Risk Assessment**: Identify technical challenges and mitigation strategies\n\n"
            "Focus on maintainability, scalability, and adherence to best practices. "
            "Consider SOLID principles, design patterns, and industry standards."
        ),
        expected_output=(
            "A detailed technical design document including:\n"
            "- System architecture diagram (described textually)\n"
            "- Component breakdown with responsibilities\n"
            "- Technology stack justification\n"
            "- Data model specifications\n"
            "- Project structure outline\n"
            "- Development phases with milestones\n"
            "- Coding standards and conventions\n"
            "- Dependency list with versions\n"
            "- Risk matrix with mitigation plans\n"
            "- API specifications (if applicable)"
        ),
        agent=agent,
        name="Code Planning",
    )


def create_code_writing_task(agent, tools=None) -> Task:
    """Implement the planned code according to specifications."""
    # ADDED: create_code_syntax_tool()
    tools = list(tools) if tools is not None else [
        create_rag_tool(),
        create_web_search_tool(),
        create_code_syntax_tool(),  # <--- NEW TOOL ADDED
    ]
    return Task(
        description=(
            "Implement clean, efficient, and well-documented code for '{topic}' based on the "
            "architecture plan. Your implementation should:\n"
            "1. **Follow the Design**: Strictly adhere to the planned architecture and specifications\n"
            "2. **Write Clean Code**: Use clear variable names, proper indentation, and consistent style\n"
            "3. **Add Documentation**: Include docstrings, inline comments, and README files\n"
            "4. **Handle Errors**: Implement proper error handling, validation, and edge case management\n"
            "5. **Optimize Performance**: Write efficient algorithms and avoid unnecessary complexity\n"
            "6. **Include Examples**: Provide usage examples and sample data where appropriate\n"
            "7. **Use Best Practices**: Follow language-specific conventions and design patterns\n"
            "8. **Make it Testable**: Write modular code that's easy to unit test\n\n"
            "Use the RAG tool to reference internal coding standards and the **Code Syntax Tool** "
            "to look up best practices, language syntax, or library documentation when needed. "
            "Prioritize readability and maintainability over cleverness."
        ),
        expected_output=(
            "Complete, production-ready code including:\n"
            "- All source code files with proper organization\n"
            "- Comprehensive docstrings for all classes and functions\n"
            "- Inline comments explaining complex logic\n"
            "- README.md with setup and usage instructions\n"
            "- requirements.txt or equivalent dependency file\n"
            "- Configuration files and environment templates\n"
            "- Usage examples and sample outputs\n"
            "- Type hints and parameter validation (where applicable)\n"
            "- Proper error messages and logging"
        ),
        agent=agent,
        tools=tools,
        name="Code Writing",
    )


def create_code_testing_task(agent, tools=None) -> Task:
    """Design and execute comprehensive testing strategy."""
    # ADDED: create_code_testing_tool(), create_web_search_tool(), create_rag_tool()
    # Removed: The default list was too small, making it more robust.
    tools = list(tools) if tools is not None else [
        create_calculator_tool(),
        create_web_search_tool(),         # Needed for finding test frameworks
        create_rag_tool(),                # Needed for internal testing standards
        create_code_testing_tool(),       # <--- NEW TOOL ADDED
    ]
    return Task(
        description=(
            "Develop and execute a comprehensive testing strategy for the '{topic}' codebase. "
            "Your testing should include:\n"
            "1. **Unit Tests**: Test individual functions and methods in isolation\n"
            "2. **Integration Tests**: Verify component interactions and data flow\n"
            "3. **Edge Cases**: Test boundary conditions, null values, and invalid inputs\n"
            "4. **Error Scenarios**: Validate error handling and exception management\n"
            "5. **Performance Tests**: Assess execution time and resource usage for critical paths\n"
            "6. **Code Coverage**: Aim for at least 80% code coverage\n"
            "7. **Documentation Tests**: Verify examples in documentation work correctly\n"
            "8. **Regression Tests**: Ensure fixes don't break existing functionality\n\n"
            "Write test cases using appropriate testing frameworks (pytest, unittest, jest, etc.). "
            "Use the **Testing Framework Tool** to research best practices and the calculator tool to validate numerical test assertions. "
            "Document all test scenarios, expected outcomes, and actual results."
        ),
        expected_output=(
            "A complete testing suite with:\n"
            "- Test plan document outlining testing strategy\n"
            "- Unit test files covering all major functions\n"
            "- Integration test scenarios\n"
            "- Edge case and error handling tests\n"
            "- Test execution report with pass/fail status\n"
            "- Code coverage metrics and analysis\n"
            "- Performance benchmarks for critical operations\n"
            "- Bug report for any issues discovered\n"
            "- Recommendations for additional testing"
        ),
        agent=agent,
        tools=tools,
        name="Code Testing",
    )


def create_code_review_task(agent, tools=None) -> Task:
    """Conduct thorough code review and provide improvement recommendations."""
    # ADDED: create_dependency_audit_tool()
    # Added: Web Search and RAG for comprehensive review context
    tools = list(tools) if tools is not None else [
        create_web_search_tool(),
        create_rag_tool(),
        create_calculator_tool(), # useful for performance/complexity estimates
        create_dependency_audit_tool(), # <--- NEW TOOL ADDED
    ]
    return Task(
        description=(
            "Perform a comprehensive code review for the '{topic}' implementation, evaluating "
            "quality, security, and maintainability. Your review should assess:\n"
            "1. **Code Quality**: Check readability, naming conventions, and style consistency\n"
            "2. **Architecture Compliance**: Verify adherence to the planned design\n"
            "3. **Best Practices**: Evaluate use of design patterns and language idioms\n"
            "4. **Performance**: Identify optimization opportunities and bottlenecks\n"
            "5. **Security**: Look for vulnerabilities, injection risks, and data exposure\n"
            "6. **Error Handling**: Review exception handling and validation logic\n"
            "7. **Documentation**: Assess clarity and completeness of comments and docstrings\n"
            "8. **Testing**: Evaluate test coverage and quality of test cases\n"
            "9. **Maintainability**: Check for code smells, duplication, and complexity\n"
            "10. **Dependencies**: Use the **Dependency Audit Tool** to review library choices, versions, and security status.\n\n"
            "Provide specific, actionable feedback with code examples. Categorize issues by "
            "severity (critical, high, medium, low) and estimate effort for fixes."
        ),
        expected_output=(
            "A detailed code review report containing:\n"
            "- Executive summary with overall quality score\n"
            "- Architecture compliance assessment\n"
            "- Critical issues (security, bugs, breaking changes)\n"
            "- High-priority improvements (performance, best practices)\n"
            "- Medium-priority suggestions (refactoring, optimization)\n"
            "- Low-priority polish items (style, naming, comments)\n"
            "- Code snippets showing problems and solutions\n"
            "- Test coverage analysis and gaps\n"
            "- **Dependency Audit findings (security and license)**\n"
            "- Final recommendation (Approve / Conditional Approval / Reject)\n"
            "- Estimated effort for remediation"
        ),
        agent=agent,
        tools=tools,
        name="Code Review",
    )


# ============================================================================
# CONVENIENCE BUILDERS (These functions remain conceptually the same)
# ============================================================================

def build_workshop_tasks(
    planner, 
    researcher, 
    writer, 
    reviewer, 
    research_tools=None
) -> List[Task]:
    """Build the complete workshop content creation task pipeline."""
    return [
        create_planning_task(planner),
        create_research_task(researcher, tools=research_tools),
        create_writing_task(writer),
        create_review_task(reviewer),
    ]


def build_code_tasks(
    code_planner,
    code_writer,
    code_tester,
    code_reviewer,
    code_tools=None
) -> List[Task]:
    """Build the complete code development task pipeline."""
    # NOTE: The agents will receive the correct tools when the `create_code_*_task` 
    # functions override the `tools=None` default with the explicit tool lists defined above.
    return [
        create_code_planning_task(code_planner),
        create_code_writing_task(code_writer, tools=code_tools),
        create_code_testing_task(code_tester, tools=code_tools),
        create_code_review_task(code_reviewer),
    ]


def build_full_workshop_pipeline(
    planner,
    researcher,
    writer,
    reviewer,
    code_planner,
    code_writer,
    code_tester,
    code_reviewer,
    research_tools=None,
    code_tools=None
) -> List[Task]:
    """Build a complete end-to-end workshop pipeline including both content and code."""
    return [
        # Content development phase
        create_planning_task(planner),
        create_research_task(researcher, tools=research_tools),
        create_writing_task(writer),
        create_review_task(reviewer),
        # Code development phase
        create_code_planning_task(code_planner),
        create_code_writing_task(code_writer, tools=code_tools),
        create_code_testing_task(code_tester, tools=code_tools),
        create_code_review_task(code_reviewer),
    ]