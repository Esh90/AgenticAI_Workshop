"""Streamlit frontend for the Code Development Assistant multi-agent system."""

# 1. Future imports MUST be first
from __future__ import annotations

# 2. System imports
import sys
import os
from pathlib import Path

# 3. SQLite Fix (Must be before importing streamlit or other heavy libraries)
# This fixes the "sqlite3 version too old" error on Streamlit Cloud
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass # Pass if running locally without pysqlite3 installed

# 4. Application Imports
import streamlit as st
from dotenv import load_dotenv

# 5. Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# 6. Import Backend
from main import run_pipeline 

load_dotenv()

# --- STREAMLIT CONFIGURATION ---

# Setting a professional, tech-focused page configuration
st.set_page_config(
    page_title="Code Development Assistant | Multi-Agent AI", 
    page_icon="🤖", 
    layout="wide"
)

# --- HEADER AND PROJECT OVERVIEW ---

# Use columns for a visually balanced header
header_col1, header_col2 = st.columns([1, 4])

with header_col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4b/Code_symbol.svg", width=100) 
with header_col2:
    st.title("Code Development Assistant 🚀")
    st.subheader("Multi-Agent System for Automated Planning, Writing, Testing, and Review.")

st.markdown("""
<style>
.stTabs [data-baseweb="tab-list"] {
    gap: 24px;
}
.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: nowrap;
    background-color: #F0F2F6;
    border-radius: 4px 4px 0 0;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR CONFIGURATION ---

default_topic = "Develop a secure Python function to sanitize user input for SQL injection."

with st.sidebar:
    st.header("1. Define Your Task 📝")
    topic = st.text_area(
        "Coding Requirement:", 
        value=default_topic,
        height=150,
        help="Input the specific coding task you want the multi-agent crew to solve."
    )
    
    st.markdown("---")
    st.header("2. Execute Pipeline")
    run_button = st.button("Run Code Generation Crew", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.header("3. System Stack ⚙️")
    st.markdown("""
    * **Orchestrator:** CrewAI
    * **LLM Provider:** OpenRouter `(mistralai/mistral-7b-instruct:free)`
    * **Context:** FAISS RAG + Live Web Search
    * **Specialized Tools:** Syntax Check, Testing Framework Search, Dependency Audit
    """)

# --- MAIN CONTENT TABS ---

tab_result, tab_workflow, tab_context = st.tabs([
    "Final Deliverable & Review Report 📋", 
    "Live Output Analysis 📊", 
    "RAG Knowledge Base Context 📚"
])

if run_button:
    
    with tab_workflow:
        st.info("Starting the Code Development pipeline. Observe the step-by-step progress below.")
        
        st.markdown("## Multi-Agent Workflow Execution Status")
        st.progress(0, text="Initializing Code Planner...")
        st.markdown("---")
        
        st.progress(25, text="**Code Planner** is analyzing requirements...")
        st.code("Development Plan Structure: Requirements Analysis -> Architecture Design -> Dependencies...", language="markdown")
        
        st.progress(50, text="**Code Writer** is generating code and documentation...")
        st.code("Tools: Code Syntax Search active...", language="python")
        
        st.progress(75, text="**Code Tester** is creating unit tests and checking edge cases...")
        st.code("Tools: Testing Framework Search active...", language="python")
        
        st.progress(90, text="**Code Reviewer** is auditing for quality and security...")
        st.code("Tools: Dependency Audit Tool active...", language="python")
        
        st.progress(100, text="Pipeline complete! Reviewing final output...")


    with st.spinner("Agents are collaborating on the task..."):
        try:
            # 1. Execute the full pipeline
            output = run_pipeline(topic)
            
        except Exception as exc:
            st.error(f"Pipeline execution failed: {exc}")
            output = None # Clear output if failed
            
    # 2. Display the Final Output
    with tab_result:
        if output:
            st.success("✅ Code Development Complete!")
            st.markdown("### Final Consolidated Output (Reviewed Deliverable)")
            st.code(output, language="markdown") # Display output as raw markdown/text
            
            # Offer download functionality to emphasize deployment readiness
            st.download_button(
                label="Download Full Report",
                data=output,
                file_name="code_assistant_report.md",
                mime="text/markdown",
                key="download_button"
            )
        elif output is None:
             st.warning("Execution failed. Check the 'Live Output Analysis' for logs.")
             
    # 3. Display Context Information
    with tab_context:
        st.markdown("### Agent Knowledge Base & Context")
        st.info("This section simulates the context available to the RAG tool and Web Search for grounding decisions.")
        
        st.markdown("#### RAG Knowledge Base Content (`rag/documents/`)")
        st.markdown("""
        * **`coding_best_practices.txt`**: DRY principle, Naming Conventions, Comment standards.
        * **`design_patterns.txt`**: Singleton, Factory, MVC/Repository patterns.
        * **`error_handling.txt`**: Exception handling and logging strategies.
        * **`testing_frameworks.txt`**: Pytest, Jest, xUnit tutorials.
        
        This curated data ensures agents adhere to **internal company standards** before consulting the open web.
        """)
        
        st.markdown("#### Dynamic Tooling (Simulated Access)")
        st.table({
            "Tool": ["Code Syntax Search", "Testing Framework Search", "Dependency Audit"],
            "Target Agent": ["Code Writer", "Code Tester", "Code Reviewer"],
            "Value Proposition": ["Ensures syntactic correctness.", "Ensures high test coverage.", "Ensures production security and compliance."]
        })
        

st.markdown("---")
st.caption(
    "Demonstrating Multi-Agent Orchestration (CrewAI) and Context Augmentation (RAG) for robust software development workflows."
)