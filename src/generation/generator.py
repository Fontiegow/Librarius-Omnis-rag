import os
import ollama
from typing import List, Dict, Any, Optional

class LoreGenerator:
    def __init__(self, model_name: str = "qwen2.5:3b", host: Optional[str] = None):
        """
        Wrapper for local LLM generation using Ollama.
        Supports explicit host targeting or OLLAMA_HOST environment variable.
        """
        self.model_name = model_name
        
        # Fallback hierarchy: Explicit arg -> Environment variable -> Default local fallback
        self.host = host or os.getenv("OLLAMA_HOST", "http://localhost:11434")
        
        # Instantiate explicit Ollama client targeting the designated host URL
        self.client = ollama.Client(host=self.host)

    def construct_prompt(self, query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """
        Combines retrieved text chunks into a structured, ground-truth context block.
        """
        context_str = ""
        for i, chunk in enumerate(retrieved_chunks, 1):
            context_str += f"\n--- Context Document [{i}] (Source: {chunk['source']}) ---\n"
            context_str += f"{chunk['text']}\n"

        system_prompt = (
            "You are Librarius Omnis, an expert Imperial Scholar and Warhammer 40,000 lore master.\n"
            "Answer the user's question accurately using ONLY the provided context snippets below.\n"
            "If the retrieved context does not contain enough information to answer the question completely, "
            "state clearly what is missing based on the available lore context.\n\n"
            f"RETRIEVED LORE CONTEXT:\n{context_str}\n\n"
            f"USER QUESTION: {query}\n\n"
            "ANSWER:"
        )
        return system_prompt

    def generate_answer(self, query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """
        Sends the augmented prompt to the designated Ollama instance and returns the generated answer.
        """
        prompt = self.construct_prompt(query, retrieved_chunks)
        
        response = self.client.generate(
            model=self.model_name,
            prompt=prompt,
            options={
                "temperature": 0.2,  # Low temperature to enforce strict adherence to context
            }
        )
        return response["response"]