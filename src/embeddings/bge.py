import torch
from sentence_transformers import SentenceTransformer
from typing import List, Union

class BGEEmbedder:
    def __init__(self, model_name: str = "BAAI/bge-m3", device: str = None):
        """
        Wrapper for BAAI/bge-m3 embedding model.
        Automatically selects CUDA (GPU) if available, otherwise defaults to CPU.
        """
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        print(f"Loading embedding model '{model_name}' on device: '{self.device}'...")
        self.model = SentenceTransformer(model_name, device=self.device)
        print("Model loaded successfully.")

    def embed_texts(self, texts: List[str], batch_size: int = 32) -> List[List[float]]:
        """
        Generates 1024-dimensional embeddings for a list of text strings.
        """
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            normalize_embeddings=True  # Normalizing simplifies cosine similarity to dot product
        )
        return embeddings.tolist()

    def embed_query(self, query: str) -> List[float]:
        """
        Generates a single 1024-dimensional embedding vector for a user query.
        """
        embedding = self.model.encode(
            query,
            normalize_embeddings=True
        )
        return embedding.tolist()