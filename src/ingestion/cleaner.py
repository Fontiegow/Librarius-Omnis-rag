import re

def clean_text(raw_text: str) -> str:
    """Normalizes raw extracted text for chunking."""
    if not raw_text:
        return ""
    
    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", raw_text)
    
    # Collapse 3+ consecutive newlines into double newlines (paragraph boundaries)
    text = re.sub(r"\n{3,}", "\n\n", text)
    
    # Strip leading/trailing whitespace
    return text.strip()