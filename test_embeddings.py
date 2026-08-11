import numpy as np
from embeddings.test_bge import BGEEmbedder

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def main():
    embedder = BGEEmbedder()

    # Define test sentences
    sentence_a = "Horus betrayed the Emperor of Mankind during the Great Crusade."
    sentence_b = "The Warmaster led a rebellion against the Imperium."
    sentence_c = "Sanguinius was the Primarch of the Blood Angels legion."
    sentence_d = "A recipe for baking chocolate fudge cookies."

    print("\nGenerating embeddings for test sentences...")
    vec_a = embedder.embed_query(sentence_a)
    vec_b = embedder.embed_query(sentence_b)
    vec_c = embedder.embed_query(sentence_c)
    vec_d = embedder.embed_query(sentence_d)

    # Compute similarity scores
    sim_a_b = cosine_similarity(vec_a, vec_b) # Same event, different wording
    sim_a_c = cosine_similarity(vec_a, vec_c) # Related lore context
    sim_a_d = cosine_similarity(vec_a, vec_d) # Completely unrelated topic

    print("\n--- SEMANTIC SIMILARITY RESULTS ---")
    print(f"Query: '{sentence_a}'\n")
    print(f"1. Related Event  ('{sentence_b}'): Similarity = {sim_a_b:.4f}")
    print(f"2. Related Lore   ('{sentence_c}'): Similarity = {sim_a_c:.4f}")
    print(f"3. Unrelated Text ('{sentence_d}'): Similarity = {sim_a_d:.4f}")

if __name__ == "__main__":
    main()