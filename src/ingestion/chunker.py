from typing import List, Dict, Any

def create_chunks(
    source_filename: str,
    text: str,
    chunk_size: int = 800,
    chunk_overlap: int = 150
) -> List[Dict[Any, Any]]:
    """
    Splits text into overlapping sliding-window chunks with metadata.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be strictly smaller than chunk_size.")
        
    chunks = []
    start = 0
    text_length = len(text)
    chunk_index = 0

    step = chunk_size - chunk_overlap

    while start < text_length:
        end = start + chunk_size
        chunk_text = text[start:end]
        
        # Don't create near-empty trailing chunks
        if len(chunk_text.strip()) > 50:
            chunk_data = {
                "chunk_id": f"{source_filename.replace('.txt', '')}_{chunk_index:04d}",
                "source": source_filename,
                "text": chunk_text.strip(),
                "start_char": start,
                "end_char": start + len(chunk_text),
                "char_length": len(chunk_text)
            }
            chunks.append(chunk_data)
            chunk_index += 1
            
        start += step

    return chunks