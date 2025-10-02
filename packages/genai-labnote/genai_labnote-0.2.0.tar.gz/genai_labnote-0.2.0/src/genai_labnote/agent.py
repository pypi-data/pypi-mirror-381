# src/genai_labnote/agent.py

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain_experimental.tools import PythonAstREPLTool
from langchain import hub

def create_agent_executor(logger_instance):
    """
    Creates a LangChain AgentExecutor with access to the lab notes and a Python REPL.
    """
    # 1. Get the API Key from the environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in environment. "
            "Please load your .env file in the notebook before running the agent."
        )

    # 2. Initialize the LLM, passing the API key directly
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=api_key,
        temperature=0
    )

    # 3. Define the tools the agent can use 
    @tool
    def search_lab_notebook(query: str) -> str:
        """
        Searches the user's past experiment logs to find relevant information.
        Use this to answer questions about past experiments, code, or results.
        """
        print(f"--- Agent is using Search Tool with query: {query} ---")
        search_results_df = logger_instance.search(query, k=3)
        if search_results_df.empty:
            return "No relevant experiments found."
        return search_results_df.to_string()

    python_repl = PythonAstREPLTool()
    tools = [search_lab_notebook, python_repl]

    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)

    # 5. Create the Agent Executor 
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    
    return agent_executor