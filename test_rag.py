import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

print("--- STARTING ISOLATED RAG TEST ---")

from src.retrieval.retriever import LoreRetriever
from src.generation.generator import LoreGenerator

print("[1/4] Loading Retriever & Embeddings...")
retriever = LoreRetriever()

print("[2/4] Executing Retrieval...")
chunks = retriever.retrieve("Who is Guilliman?", top_k=3)
print(f"   -> Retrieved {len(chunks)} chunks successfully.")

print("[3/4] Loading Generator...")
generator = LoreGenerator(model_name="qwen2.5:3b")

print("[4/4] Generating Response...")
answer = generator.generate_answer("Who is Guilliman?", chunks)

print("\n--- TEST SUCCESSFUL ---")
print(answer)