import os
import json
from src.ingestion.cleaner import clean_text
from src.ingestion.chunker import create_chunks

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
OUTPUT_FILE = os.path.join(PROCESSED_DIR, "chunks.json")

def main():
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    all_chunks = []
    
    raw_files = [f for f in os.listdir(RAW_DIR) if f.endswith(".txt")]
    print(f"Found {len(raw_files)} raw files in '{RAW_DIR}'. Starting preprocessing...\n")

    for filename in raw_files:
        filepath = os.path.join(RAW_DIR, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            raw_text = f.read()
            
        cleaned_text = clean_text(raw_text)
        chunks = create_chunks(
            source_filename=filename,
            text=cleaned_text,
            chunk_size=800,
            chunk_overlap=150
        )
        
        all_chunks.extend(chunks)
        print(f"Processed '{filename}': generated {len(chunks)} chunks.")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
        
    print(f"\n[SUCCESS] Ingestion complete. Created total {len(all_chunks)} chunks.")
    print(f"Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()