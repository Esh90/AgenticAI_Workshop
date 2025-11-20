# Code Development Assistant: Multi-Agent System
## Complete Project Documentation

---

## 1. Project Overview

The **Code Development Assistant** is a multi-agent AI system designed to help developers write, understand, and improve code. It orchestrates four specialized agents to transform a coding task into working, tested, and documented code.

### Core Workflow
**Code Planner** → **Code Writer** → **Code Tester** → **Code Reviewer**

### Purpose
Enable faster and smarter code development by leveraging AI agents that collaborate on planning, implementation, testing, and quality assurance.

### Key Technologies
- **Framework:** CrewAI
- **LLM:** Meta-Llama 3.3 70B (via OpenRouter)
- **RAG:** FAISS vector store with LangChain
- **Frontend:** Streamlit
- **APIs:** DuckDuckGo, Calculator tools
- **Python Version:** 3.10+

---

## 2. Team Structure & Responsibilities

### Team Member Assignments

| Team Member | Agent Role | Responsibilities |
|-------------|-----------|-----------------|
| **You (Lead)** | Code Planner + Orchestrator | Project setup, agent orchestration, RAG pipeline, deployment |
| **Member 1** | Code Writer | Implementation tool, syntax checking, code generation |
| **Member 2** | Code Tester + Code Reviewer | Testing tool, code quality checks, UI refinement |

### Collaboration Points
- Daily: Git commits with clear messages
- Mid-week: 15-min sync on integration issues
- End-week: Full pipeline testing
- Pre-deployment: Code review from all members

---

## 3. Detailed Agent Specifications

### 3.1 Code Planner Agent
**Purpose:** Analyze coding requirements and create a structured plan

**System Prompt Template:**
```
You are the Code Planner. Your role is to:
1. Analyze the coding requirement or problem
2. Break it down into smaller tasks
3. Suggest the best approach and design pattern
4. Outline the file structure needed
5. List dependencies and libraries required

Format output as:
- Problem Analysis:
- Suggested Approach:
- Design Pattern:
- File Structure:
- Required Libraries:
- Implementation Steps (1-5):
- Estimated Complexity:
```

**Input:** Coding task/requirement
**Output:** Structured development plan
**Tools:** Local RAG search, web search, calculator
**Owner:** You (can optimize based on crew feedback)

---

### 3.2 Code Writer Agent
**Purpose:** Generate clean, well-structured code based on the plan

**System Prompt Template:**
```
You are the Code Writer. Your role is to:
1. Follow the development plan from the planner
2. Write clean, readable code with best practices
3. Add comments and docstrings
4. Handle error cases
5. Ensure code is modular and reusable

Format output as:
- Code (with line numbers):
- Key Features:
- Dependencies Used:
- Installation Instructions:
- Usage Example:
- Notes:
```

**Input:** Development plan from Planner
**Output:** Complete, working code
**Tools:** Web search for syntax, RAG, calculator
**Owner:** Team Member 1

**Key Tool:** `code_syntax_tool.py`
```python
# Searches for correct syntax and best practices
# Validates code patterns
# Returns code examples
```

---

### 3.3 Code Tester Agent
**Purpose:** Create test cases and verify code functionality

**System Prompt Template:**
```
You are the Code Tester. Your role is to:
1. Review the code for potential issues
2. Create comprehensive test cases
3. Identify edge cases
4. Suggest test scenarios
5. Check for common bugs

Format output as:
- Test Cases (with descriptions):
- Edge Cases to Handle:
- Expected Vs Actual Results:
- Potential Bugs Found:
- Test Coverage Analysis:
- Recommended Fixes:
```

**Input:** Code from Code Writer
**Output:** Test scenarios and bug report
**Tools:** Web search for testing patterns, RAG, calculator
**Owner:** Team Member 2

**Key Tool:** `code_testing_tool.py`
```python
# Searches for testing frameworks and best practices
# Generates test case templates
# Checks for common vulnerabilities
```

---

### 3.4 Code Reviewer Agent
**Purpose:** Review code quality and provide optimization suggestions

**System Prompt Template:**
```
You are the Code Reviewer. Your role is to:
1. Review code for quality and standards
2. Check for performance issues
3. Suggest improvements and optimizations
4. Ensure code follows best practices
5. Provide final approval or feedback

Format output as:
- Code Quality Score (1-10):
- Performance Assessment:
- Best Practices Compliance:
- Security Issues (if any):
- Suggested Optimizations:
- Final Recommendations:
- Ready for Production: Yes/No
```

**Input:** Code + Test results
**Output:** Code review report with recommendations
**Tools:** Web search for optimization patterns, RAG, calculator
**Owner:** Team Member 2

**Key Tool:** Already uses existing RAG + web search tools

---

## 4. Project Structure

```
code-dev-assistant/
├── .env.example
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
├── main.py
├── crew.py
├── tasks.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── agents/
│   ├── __init__.py
│   ├── code_planner.py
│   ├── code_writer.py
│   ├── code_tester.py
│   └── code_reviewer.py
│
├── tools/
│   ├── __init__.py
│   ├── rag_tool.py
│   ├── web_search.py
│   ├── calculator.py
│   ├── code_syntax_tool.py
│   └── code_testing_tool.py
│
├── rag/
│   ├── build_vector_db.py
│   ├── documents/
│   │   ├── coding_best_practices.txt
│   │   ├── design_patterns.txt
│   │   ├── error_handling.txt
│   │   └── testing_frameworks.txt
│   └── vectorstore/
│       └── faiss_index/
│
├── frontend/
│   └── app.py
│
└── tests/
    ├── test_crew.py
    ├── test_agents.py
    └── test_tools.py
```

---

## 5. Custom Tools Development

### 5.1 Code Syntax Tool
**Location:** `tools/code_syntax_tool.py`
**Owner:** Team Member 1

```python
from crewai_tools import tool

@tool("Code Syntax Search")
def code_syntax_search(query: str) -> str:
    """
    Search for correct syntax, code patterns, and best practices.
    
    Args:
        query: Syntax/pattern query (e.g., "Python list comprehension")
    
    Returns:
        Code examples and syntax guidance
    """
    # Uses DuckDuckGo to find syntax examples
    # Searches for best practices and common patterns
    # Returns formatted code snippets and explanations
    pass
```

**Features:**
- Finds correct syntax for programming concepts
- Searches for code design patterns
- Returns code examples from Stack Overflow and docs
- Provides best practice guidance

---

### 5.2 Code Testing Tool
**Location:** `tools/code_testing_tool.py`
**Owner:** Team Member 2

```python
from crewai_tools import tool

@tool("Testing Framework Search")
def testing_framework_search(query: str) -> str:
    """
    Search for testing frameworks, test patterns, and testing best practices.
    
    Args:
        query: Testing query (e.g., "Python unit testing pytest")
    
    Returns:
        Testing frameworks and test examples
    """
    # Searches for testing frameworks
    # Finds test case examples
    # Returns common testing patterns
    pass
```

**Features:**
- Finds testing frameworks for different languages
- Searches for test case examples
- Retrieves security testing patterns
- Returns performance testing guidelines

---

## 6. RAG Knowledge Base Setup

### 6.1 Knowledge Base Documents
Place in `rag/documents/`:

**coding_best_practices.txt**
- DRY principle (Don't Repeat Yourself)
- Code comments and documentation standards
- Naming conventions
- Function/method design guidelines

**design_patterns.txt**
- Singleton pattern
- Factory pattern
- Observer pattern
- MVC/MVVM architecture
- Repository pattern

**error_handling.txt**
- Exception handling best practices
- Logging strategies
- Try-catch patterns
- Error messages and user feedback

**testing_frameworks.txt**
- Jest (JavaScript)
- pytest (Python)
- JUnit (Java)
- xUnit (.NET)
- Testing best practices and coverage goals

### 6.2 Building the Vector Store
```bash
# Run once during setup
python rag/build_vector_db.py

# Re-run if knowledge base changes
python rag/build_vector_db.py --rebuild
```

---

## 7. Task Definitions

### Task 1: Code Planning
**Agent:** Code Planner
**Description:** Analyze requirements and create development plan
**Expected Output:** Structured development plan (300-500 words)

### Task 2: Code Writing
**Agent:** Code Writer
**Description:** Write clean, well-documented code following the plan
**Expected Output:** Complete working code with documentation

### Task 3: Code Testing
**Agent:** Code Tester
**Description:** Create test cases and identify potential issues
**Expected Output:** Test scenarios and bug report (200-400 words)

### Task 4: Code Review
**Agent:** Code Reviewer
**Description:** Review code quality and provide optimization suggestions
**Expected Output:** Code review report with score and recommendations

---

## 8. Installation & Setup

### 8.1 Prerequisites
- Python 3.10 or higher
- OpenRouter API key (free tier at https://openrouter.ai)
- Git for version control
- Virtual environment tool (venv, conda, or pipenv)

### 8.2 Step-by-Step Setup

**Step 1: Clone Repository**
```bash
git clone https://github.com/your-org/code-dev-assistant.git
cd code-dev-assistant
```

**Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Configure Environment**
```bash
cp .env.example .env
# Edit .env and add your OpenRouter API key
# OPENROUTER_API_KEY=your_key_here
```

**Step 5: Build RAG Vector Store**
```bash
python rag/build_vector_db.py
```

**Step 6: Verify Setup**
```bash
python main.py --task "Create a Python function that reverses a string"
```

---

## 9. Running the System

### 9.1 Command Line Interface
```bash
# Basic usage
python main.py --task "Your coding task here"

# Example
python main.py --task "Write a Python function to check if a number is prime"

# With custom output file
python main.py --task "Your task" --output results.txt

# Verbose mode for debugging
python main.py --task "Your task" --verbose
```

### 9.2 Streamlit Web Interface
```bash
# Launch UI
python -m streamlit run frontend/app.py

# Access at: http://localhost:8501
```

**Streamlit Features:**
- Sidebar input for coding task
- Real-time agent execution status
- Tabbed output view (Plan → Code → Tests → Review)
- Code syntax highlighting
- Copy to clipboard button
- Export results

### 9.3 Programmatic Usage
```python
from main import run_pipeline

result = run_pipeline(
    task="Create a REST API endpoint in FastAPI",
    verbose=True,
    output_format="json"
)

print(result)
```

---

## 10. Customization Guide

### 10.1 Modifying Agent Prompts

**File:** `agents/code_planner.py`

Update the `system_prompt` variable in each agent file:
```python
system_prompt = """
You are the Code Planner specialized in [LANGUAGE/FRAMEWORK].
Your role is to...
"""
```

### 10.2 Adding New Tools

1. Create tool file: `tools/my_new_tool.py`
2. Implement tool function with @tool decorator
3. Register in `tools/__init__.py`
4. Add to agent in `agents/[agent_name].py`

### 10.3 Extending RAG Knowledge Base

1. Add document files to `rag/documents/`
2. Re-build vector store: `python rag/build_vector_db.py`
3. Test with relevant queries

### 10.4 Adjusting Task Parameters

**File:** `tasks.py`

Modify expected_output and descriptions:
```python
task_planning = Task(
    description="Analyze requirements and create development plan",
    expected_output="300-500 word structured development plan",
    agent=code_planner_agent,
)
```

---

## 11. Testing Strategy

### 11.1 Unit Tests
```bash
# Run individual agent tests
python -m pytest tests/test_agents.py -v

# Run tool tests
python -m pytest tests/test_tools.py -v
```

### 11.2 Integration Tests
```bash
# Full pipeline test
python -m pytest tests/test_crew.py -v
```

### 11.3 Manual Testing Scenarios
1. **Simple Task:** "Create a Python function to add two numbers"
2. **Medium Task:** "Build a REST API endpoint with error handling"
3. **Complex Task:** "Design a database schema for a blog application with comments"
4. **Real-world Task:** "Refactor legacy code for better performance"

---

## 12. Deployment Guide

### 12.1 Streamlit Community Cloud (Recommended)

**Prerequisites:**
- GitHub account with public repo
- Streamlit Community Cloud account (free)

**Steps:**
1. Push repo to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Select your repository and `frontend/app.py`
5. Configure secrets (Settings → Secrets):
   ```
   OPENROUTER_API_KEY = "your_key"
   ```
6. Deploy!

**URL Pattern:** `https://[username]-[appname].streamlit.app`

### 12.2 Docker Containerization

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python rag/build_vector_db.py

EXPOSE 8501

CMD ["streamlit", "run", "frontend/app.py"]
```

**Build & Run:**
```bash
docker build -t code-dev-assistant .
docker run -e OPENROUTER_API_KEY=your_key -p 8501:8501 code-dev-assistant
```

### 12.3 Cloud Platform Options

| Platform | Best For | Difficulty |
|----------|----------|-----------|
| Streamlit Cloud | Quick demos | Easy |
| AWS App Runner | Production apps | Medium |
| Google Cloud Run | Scalable workloads | Medium |
| Heroku | Simple deployment | Easy |

---

## 13. Git Workflow & Collaboration

### 13.1 Repository Setup
```bash
# Initialize repo (Team Lead)
git init
git add .
git commit -m "Initial commit: Code Development Assistant template"
git branch -M main
git remote add origin https://github.com/your-org/code-dev-assistant.git
git push -u origin main
```

### 13.2 Branch Strategy
```
main (stable, deployed)
├── develop (integration branch)
│   ├── feature/code-writer (Member 1)
│   ├── feature/code-tester (Member 2)
│   ├── feature/code-reviewer (Member 2)
│   └── feature/ui-design (Member 2)
```

### 13.3 Daily Workflow
```bash
# Pull latest
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: add [specific feature]"

# Push and create pull request
git push origin feature/your-feature
```

### 13.4 Commit Message Convention
```
feat: add new agent feature
fix: fix bug in code generation
docs: update README
refactor: improve code structure
test: add test cases
chore: update dependencies
```

---

## 14. Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| OPENROUTER_API_KEY not found | Missing .env file | Copy .env.example to .env and add key |
| FAISS index not found | RAG not built | Run `python rag/build_vector_db.py` |
| Agent timeouts | LLM taking too long | Reduce token limits in config/settings.py |
| Tool not registered | Missing import | Check tools/__init__.py imports |
| Streamlit errors | Module not found | Reinstall requirements in venv |

### Debug Mode
```bash
# Enable verbose logging
python main.py --task "test" --verbose --debug

# Check environment
python -c "import os; print(os.getenv('OPENROUTER_API_KEY'))"
```

---

## 15. Success Metrics

### Quality Checklist
- [ ] Code Planner generates coherent plans
- [ ] Code Writer produces working, readable code
- [ ] Code Tester identifies real issues
- [ ] Code Reviewer provides valuable feedback
- [ ] Total runtime < 3 minutes per pipeline execution
- [ ] RAG retrieval adds meaningful context to responses

### Testing Outcomes
- [ ] 5+ test scenarios run successfully
- [ ] All tools function without errors
- [ ] UI displays all agent outputs clearly
- [ ] Generated code is actually executable

---

## 16. Next Steps & Roadmap

### Phase 1: Foundation (Week 1)
- [x] Project setup and documentation
- [x] Agent configuration
- [x] Tool development
- [x] Local testing

### Phase 2: Integration (Week 2)
- [ ] Team member coordination
- [ ] Git workflow implementation
- [ ] Full pipeline testing
- [ ] Prompt optimization

### Phase 3: Enhancement (Week 3)
- [ ] Add multiple language support
- [ ] Implement code execution sandbox
- [ ] Create performance metrics
- [ ] Add export to GitHub functionality

### Phase 4: Deployment (Week 4)
- [ ] Containerization
- [ ] Cloud deployment
- [ ] Performance optimization
- [ ] Public repository release

### Future Enhancements
- Support for multiple programming languages
- Integration with GitHub for direct PR creation
- Code refactoring suggestions
- Performance profiling and optimization
- Security vulnerability scanning
- Documentation generation from code

---

## 17. Resources & References

### Documentation
- CrewAI Official: https://docs.crewai.com
- LangChain Docs: https://python.langchain.com
- FAISS Documentation: https://github.com/facebookresearch/faiss
- Streamlit Docs: https://docs.streamlit.io

### API References
- OpenRouter: https://openrouter.ai/docs
- DuckDuckGo API: https://duckduckgo.com/api

---

## 18. Contact & Support

### Team Contacts
- **Team Lead:** [Your Name] - Project orchestration, RAG, deployment
- **Member 1:** [Name] - Code writing tools, syntax checking
- **Member 2:** [Name] - Testing tools, code review, UI/frontend

### Communication Channels
- GitHub Issues: Bug reports and feature requests
- Weekly Sync: [Day/Time]
- Emergency Contact: [Slack/Discord channel]

---

## 19. License & Attribution

This project is built upon the CrewAI Workshop template with custom extensions for code development workflows.

**License:** [MIT/Apache 2.0 - Your Choice]

**Attribution:** Built by [Team Name] | Powered by CrewAI, LangChain, and Streamlit

---

## 20. Appendix: Quick Reference

### Environment Variables
```
OPENROUTER_API_KEY = your_api_key
OPENROUTER_MODEL = meta-llama/llama-3.3-70b-instruct:free
RAG_CHUNK_SIZE = 1000
RAG_CHUNK_OVERLAP = 200
LLM_TEMPERATURE = 0.7
MAX_TOKENS = 4000
```

### Key Commands
```bash
# Setup
python -m venv .venv
pip install -r requirements.txt
python rag/build_vector_db.py

# Run
python main.py --task "Your coding task"
python -m streamlit run frontend/app.py

# Test
python -m pytest tests/ -v

# Deploy
docker build -t code-dev-assistant .
```

### File Ownership Summary
| File | Owner |
|------|-------|
| agents/code_planner.py | Lead |
| agents/code_writer.py | Member 1 |
| agents/code_tester.py | Member 2 |
| agents/code_reviewer.py | Member 2 |
| tools/code_syntax_tool.py | Member 1 |
| tools/code_testing_tool.py | Member 2 |
| frontend/app.py | Member 2 |
| crew.py, main.py | Lead |

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Status:** Ready for Development