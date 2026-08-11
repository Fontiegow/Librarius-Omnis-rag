from src.retrieval.retriever import LoreRetriever
from src.generation.generator import LoreGenerator

def main():
    print("Initializing Librarius Omnis RAG Engine...")
    retriever = LoreRetriever()
    generator = LoreGenerator(model_name="qwen2.5:3b")  # Update model_name to match your installed Ollama model

    while True:
        print("\n" + "="*80)
        user_query = input("Ask Librarius Omnis a question (or type 'exit' to quit): ")
        if user_query.strip().lower() in ["exit", "quit"]:
            break

        print("\n[1/2] Retrieving relevant lore chunks from Qdrant...")
        retrieved_chunks = retriever.retrieve(user_query, top_k=3)
        
        print(f"Retrieved {len(retrieved_chunks)} relevant chunks.")
        for chunk in retrieved_chunks:
            print(f" - [{chunk['source']}] Score: {chunk['score']}")

        print("\n[2/2] Generating answer via local LLM (Ollama)...")
        answer = generator.generate_answer(user_query, retrieved_chunks)

        print("\n" + "-"*40 + " LIBRARIUS OMNIS " + "-"*40)
        print(answer)
        print("-"*97)

if __name__ == "__main__":
    main()