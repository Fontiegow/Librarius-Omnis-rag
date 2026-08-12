import os
from typing import List, Dict, Any, Optional
from qdrant_client import QdrantClient
from src.embeddings.bge import BGEEmbedder

class LoreRetriever:
    def __init__(
        self,
        collection_name: str = "warhammer_lore",
        host: Optional[str] = None,
        port: Optional[int] = None,
        embedder: Optional[BGEEmbedder] = None
    ):
        self.collection_name = collection_name
        
        # Fallback hierarchy: Explicit arg -> Environment variable -> Default local fallback
        qdrant_host = host or os.getenv("QDRANT_HOST", "localhost")
        qdrant_port = port or int(os.getenv("QDRANT_PORT", 6333))

        self.client = QdrantClient(host=qdrant_host, port=qdrant_port)

        if embedder is None:
            self.embedder = BGEEmbedder(device="cpu")
        else:
            self.embedder = embedder

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        query_vector = self.embedder.embed_query(query)

        response = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k
        )

        retrieved_chunks = []
        for hit in response.points:
            payload = hit.payload or {}
            retrieved_chunks.append({
                "score": round(hit.score, 4),
                "chunk_id": payload.get("chunk_id"),
                "source": payload.get("source", "Unknown Source"),
                "text": payload.get("text", ""),
                "start_char": payload.get("start_char"),
                "end_char": payload.get("end_char")
            })

        return retrieved_chunks