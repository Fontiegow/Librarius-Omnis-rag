import os
import sys
import time
import requests
from bs4 import BeautifulSoup

# Force UTF-8 stdout encoding for Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Base endpoint for Warhammer 40K Fandom Wiki
API_URL = "https://warhammer40k.fandom.com/api.php"

# Seed list of core Warhammer 40K topics to start your knowledge base
TARGET_TITLES = [
    "Horus Heresy",
    "Horus Lupercal",
    "Emperor of Mankind",
    "Space Marine Legions",
    "Ultramarines",
    "Imperium of Man",
    "Chaos Gods",
    "Battle of Terra",
    "Adeptus Astartes",
    "Eldar"
]

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_page_text(title: str) -> str | None:
    """Fetches full article content and strips HTML tags cleanly."""
    params = {
        "action": "parse",
        "format": "json",
        "page": title,
        "prop": "text",
        "redirects": True
    }
    headers = {
        "User-Agent": "Warhammer40K-RAG-LearningProject/1.0 (educational use)"
    }
    
    try:
        response = requests.get(API_URL, params=params, headers=headers)
        if response.status_code != 200:
            print(f"  [ERROR] Failed to fetch '{title}': HTTP {response.status_code}")
            return None
            
        data = response.json()
        
        # Check if page was not found
        if "error" in data:
            print(f"  [WARN] API Error for '{title}': {data['error'].get('info')}")
            return None
            
        html_content = data.get("parse", {}).get("text", {}).get("*", "")
        if not html_content:
            print(f"  [WARN] Empty content returned for '{title}'.")
            return None
            
        # Parse HTML and remove non-content elements
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Strip out unwanted elements (tables, sidebars, scripts, references, footers)
        for element in soup(["script", "style", "table", "aside", "figure", "sup", "nav", "form"]):
            element.decompose()
            
        text = soup.get_text(separator="\n")
        
        # Clean up blank lines and white spaces
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        cleaned_text = "\n\n".join(lines)
        
        return cleaned_text

    except Exception as e:
        print(f"  [ERROR] Exception while fetching '{title}': {e}")
        return None

def main():
    print(f"Starting data collection into '{OUTPUT_DIR}'...\n")
    for title in TARGET_TITLES:
        print(f"Fetching: {title}...")
        text = fetch_page_text(title)
        
        if text:
            filename = title.lower().replace(" ", "_") + ".txt"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  [OK] Saved to {filepath} ({len(text)} chars)")
        else:
            print(f"  [FAIL] Failed to save content for {title}")
        
        time.sleep(0.5)
        
    print("\nData collection complete.")

if __name__ == "__main__":
    main()