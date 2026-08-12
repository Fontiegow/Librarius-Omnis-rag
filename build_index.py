import json
import os
import time
from src.embeddings.bge import BGEEmbedder  # Fixed import path
from src.vectorstore.qdrant import QdrantVectorStore

CHUNKS_FILE = "data/processed/chunks.json"

def main():
    if not os.path.exists(CHUNKS_FILE):
        print(f"[ERROR] '{CHUNKS_FILE}' not found. Please run run_ingestion.py first.")
        return

    # 1. Load Chunks
    print(f"Loading chunks from '{CHUNKS_FILE}'...")
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    print(f"Loaded {len(chunks)} chunks.")

    # 2. Extract Text Strings
    texts = [c["text"] for c in chunks]

    # 3. Generate Embeddings using GPU
    start_time = time.time()
    embedder = BGEEmbedder()
    print("\nGenerating BGE-M3 embeddings for all chunks on GPU...")
    embeddings = embedder.embed_texts(texts, batch_size=32)
    print(f"Generated {len(embeddings)} vectors in {time.time() - start_time:.2f} seconds.")

    # 4. Initialize Qdrant (HTTP) and Index Data
    vector_store = QdrantVectorStore()
    vector_store.create_collection()
    vector_store.upsert_chunks(chunks, embeddings)

    print("\n[SUCCESS] Knowledge Base built and indexed in Docker Qdrant database!")

if __name__ == "__main__":
    main()