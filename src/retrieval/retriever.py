from typing import List, Dict, Any
from qdrant_client import QdrantClient
from src.embeddings.bge import BGEEmbedder

class LoreRetriever:
    def __init__(
        self,
        collection_name: str = "warhammer_lore",
        qdrant_path: str = "qdrant_db",
        embedder: BGEEmbedder = None
    ):
        """
        Initializes the retriever with the local Qdrant instance and BGE-M3 embedder.
        """
        self.collection_name = collection_name
        self.client = QdrantClient(path=qdrant_path)
        
        # Reuse existing embedder if provided, otherwise load BGE-M3
        if embedder is None:
            self.embedder = BGEEmbedder()
        else:
            self.embedder = embedder

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Embeds the user query, executes similarity search in Qdrant using query_points,
        and returns the Top-K relevant text chunks with similarity scores.
        """
        # 1. Embed user query into a 1024-dim vector
        query_vector = self.embedder.embed_query(query)

        # 2. Perform Cosine Similarity search using query_points
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k
        )

        # 3. Format and extract payloads from returned points
        retrieved_chunks = []
        for hit in response.points:
            retrieved_chunks.append({
                "score": round(hit.score, 4),
                "chunk_id": hit.payload.get("chunk_id"),
                "source": hit.payload.get("source"),
                "text": hit.payload.get("text"),
                "start_char": hit.payload.get("start_char"),
                "end_char": hit.payload.get("end_char")
            })

        return retrieved_chunks