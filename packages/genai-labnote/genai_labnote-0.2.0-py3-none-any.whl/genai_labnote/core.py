# src/genai_labnote/core.py

from .storage import VectorStore
from .llm import LLMInterface
from .agent import create_agent_executor # Import our new agent creator

class ExperimentLogger:
    _instance = None
    _agent_executor = None # Cache for the agent executor

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ExperimentLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, storage_path="."):
        if not hasattr(self, 'initialized'):
            print("Initializing GenAI Lab Notebook...")
            self.storage_path = storage_path
            self.store = VectorStore(storage_path)
            self.llm = LLMInterface()
            self.initialized = True
            print("Ready to log experiments and run agent.")

    def log(self, code, output, notes=""):
        # This method remains unchanged
        print("\n Starting new log entry...")
        summary = self.llm.summarize(code, output)
        print(f" Generated Summary: {summary}")
        entry_data = {"code": code, "output": output, "user_notes": notes}
        self.store.add_entry(entry_data, summary)
    
    def search(self, query, k=3):
        """Provides direct access to the vector search for the agent's tools."""
        return self.store.search(query, k)

    def show_all(self):
        return self.store.get_all_logs()

    def run_agent(self, question: str):
        """
        Initializes and runs the AI agent to answer a complex question.
        """
        print(f"\n Agent activated. Answering question: '{question}'")
        
        # Initialize the agent executor only once and cache it
        if self._agent_executor is None:
            print("Creating agent for the first time...")
            self._agent_executor = create_agent_executor(self)

        try:
            response = self._agent_executor.invoke({"input": question})
            return response.get("output")
        except Exception as e:
            return f"An error occurred while running the agent: {e}"