from src.retrieval.retriever import LoreRetriever

def main():
    retriever = LoreRetriever()

    test_queries = [
        "Why did Horus betray the Emperor?",
        "What are the origins of the Ultramarines legion?",
        "Who is the master of the Blood Angels?"
    ]

    for query in test_queries:
        print("\n" + "="*80)
        print(f"QUERY: {query}")
        print("="*80)

        results = retriever.retrieve(query, top_k=2)

        for i, hit in enumerate(results, 1):
            print(f"\n--- [Rank {i}] Score: {hit['score']} | Source: {hit['source']} | ID: {hit['chunk_id']} ---")
            print(f"Text Snippet:\n{hit['text'][:300]}...")

if __name__ == "__main__":
    main()