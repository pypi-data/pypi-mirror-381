# src/genai_labnote/llm.py

from transformers import pipeline

class LLMInterface:
    def __init__(self):
        """
        Initializes the interface with only the local summarization model.
        The generative AI is now handled by the LangChain agent.
        """
        print("Initializing LLM Interface for local summarization...")
        self.summarization_pipeline = pipeline(
            "summarization", 
            model="sshleifer/distilbart-cnn-6-6"
        )
        print("Local summarizer ready.")

    def summarize(self, code, output):
        text_to_summarize = f"PYTHON CODE:\n```python\n{code}\n```\n\nOUTPUT:\n```\n{output}\n```"
        if len(text_to_summarize) > 1024:
            text_to_summarize = text_to_summarize[:1024]
        summary = self.summarization_pipeline(text_to_summarize, max_length=60, min_length=15, do_sample=False)
        return summary[0]['summary_text']