import os
import json
import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from datetime import datetime

class VectorStore:
    def __init__(self, storage_path="."):
        self.storage_path = storage_path
        self.log_file = os.path.join(storage_path, "lab_notes.jsonl")
        self.index_file = os.path.join(storage_path, "lab_notes.index")
        
        # Use a small, efficient model for embeddings
        self.embed_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = self.embed_model.get_sentence_embedding_dimension()
        
        self.index = self._load_index()
        self.logs = self._load_logs()
        
    def _load_index(self):
        if os.path.exists(self.index_file):
            return faiss.read_index(self.index_file)
        else:
            return faiss.IndexFlatL2(self.dimension)

    def _load_logs(self):
        logs = []
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                for line in f:
                    logs.append(json.loads(line))
        return logs
        
    def add_entry(self, entry_data, summary):
        """Adds a new experiment entry and updates the index."""
        # 1. Create the text to be embedded (summary + key data)
        text_to_embed = f"Summary: {summary}\nCode: {entry_data.get('code', '')}\nOutput: {entry_data.get('output', '')}"
        
        # 2. Generate embedding
        embedding = self.embed_model.encode([text_to_embed])
        
        # 3. Add to FAISS index
        self.index.add(np.array(embedding, dtype=np.float32))
        
        # 4. Save the log entry
        log_entry = {
            "id": self.index.ntotal - 1, # Use the FAISS index position as ID
            "timestamp": datetime.now().isoformat(),
            "summary": summary,
            **entry_data
        }
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        self.logs.append(log_entry)
        self.save_index()
        
        print(f"Experiment logged with ID {log_entry['id']}.")
        
    def search(self, query, k=5):
        """Searches the vector store for a given query."""
        if self.index.ntotal == 0:
            return "No logs found to search."
            
        query_embedding = self.embed_model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding, dtype=np.float32), k)
        
        results = []
        for i in indices[0]:
            if i < len(self.logs):
                results.append(self.logs[i])
        
        return pd.DataFrame(results)

    def save_index(self):
        faiss.write_index(self.index, self.index_file)

    def get_all_logs(self):
        return pd.DataFrame(self.logs)