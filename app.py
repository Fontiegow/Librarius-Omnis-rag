import os
import sys

# 1. Enforce single-threaded OpenMP/MKL via environment variables BEFORE importing torch
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 2. Safely limit PyTorch thread pools (guarded against Streamlit script re-runs)
import torch
try:
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
except RuntimeError:
    pass  # Already set in this Python process on first run

# Rest of app.py stays the same...
import streamlit as st
import base64
import random
import json
import re

# 1. Page Config MUST be the very first Streamlit command
st.set_page_config(
    page_title="Librarius Omnis",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Global Resource Caching
# Loads models ONCE on startup in the main thread to prevent thread-spawn crashes
@st.cache_resource(show_spinner="Initializing Cogitator Core (Loading Embeddings & Ollama)...")
def init_rag_engine():
    from src.retrieval.retriever import LoreRetriever
    from src.generation.generator import LoreGenerator
    
    # Ensure retriever targets the running Qdrant Docker container on port 6333
    retriever = LoreRetriever(host="localhost", port=6333)
    generator = LoreGenerator(model_name="qwen2.5:3b")
    
    return retriever, generator

# Initialize backend instances
retriever, generator = init_rag_engine()

# Helper Functions
def get_random_background():
    bg_dir = "assets/backgrounds"
    if os.path.exists(bg_dir):
        images = [f for f in os.listdir(bg_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if images:
            return os.path.join(bg_dir, random.choice(images))
    return None

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def inject_custom_css():
    bg_image_path = get_random_background()
    bg_css = ""
    
    if bg_image_path:
        bin_str = get_base64_of_bin_file(bg_image_path)
        bg_css = f"""
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
        }}
        """

    custom_css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Share+Tech+Mono&display=swap');

    {bg_css}

    /* Global Font Settings */
    html, body, [class*="css"] {{
        font-family: 'Share Tech Mono', monospace;
        color: #e2d1a6;
    }}

    /* Headers */
    h1, h2, h3 {{
        font-family: 'Cinzel Decorative', serif;
        color: #d4af37 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }}

    /* Solid Dark Input Boxes */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div > div,
    div[data-baseweb="select"] {{
        background-color: rgba(14, 15, 20, 0.95) !important;
        backdrop-filter: blur(4px) !important;
        border: 1px solid #5c4a1d !important;
        color: #d4af37 !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.8) !important;
    }}

    /* Dropdown Options */
    ul[data-baseweb="menu"] {{
        background-color: #0e0f14 !important;
        border: 1px solid #5c4a1d !important;
    }}

    /* Buttons */
    .stButton > button {{
        background: rgba(40, 32, 15, 0.95) !important;
        color: #e2d1a6 !important;
        border: 1px solid #d4af37 !important;
        font-family: 'Cinzel Decorative', serif !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.8) !important;
    }}
    .stButton > button:hover {{
        background: rgba(92, 74, 29, 0.95) !important;
        border-color: #ffb000 !important;
        color: #ffffff !important;
    }}

    /* Metric Boxes */
    div[data-testid="stMetricValue"] {{
        color: #ffb000 !important;
    }}

    /* Expander Darkening */
    div[data-testid="stExpander"] {{
        background-color: rgba(14, 15, 20, 0.92) !important;
        border: 1px solid #5c4a1d !important;
    }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

inject_custom_css()

def load_eval_questions():
    eval_path = "evals/questions.json"
    if os.path.exists(eval_path):
        with open(eval_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        categories = {}
        for item in data:
            cat = item.get("metadatacategory", "Basic")
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item["question"])
        return categories
    return {}

eval_data = load_eval_questions()

with st.sidebar:
    st.header("Terminal Uplink")
    st.markdown("---")
    
    selected_question = ""
    if eval_data:
        st.subheader("Standard Queries")
        selected_category = st.selectbox("Select Threat Category", list(eval_data.keys()), key="sidebar_category")
        selected_question = st.selectbox("Select Query", eval_data[selected_category], key="sidebar_query")

def render_timeline(retrieved_text=""):
    eras = {
        "M30": {"label": "M30: Great Crusade", "regex": r"M30|Great Crusade"},
        "M31": {"label": "M31: Horus Heresy", "regex": r"M31|Horus Heresy|Siege of Terra"},
        "M41": {"label": "M41: End Times", "regex": r"M41|13th Black Crusade"},
        "M42": {"label": "M42: Era Indomitus", "regex": r"M42|Indomitus|Guilliman"}
    }

    timeline_html = "<div style='display: flex; justify-content: space-between; border-bottom: 2px solid #5c4a1d; padding-bottom: 10px; margin-top: 20px; background-color: rgba(10, 10, 14, 0.85); padding: 10px; border-radius: 4px;'>"
    
    for key, data in eras.items():
        is_active = bool(re.search(data["regex"], retrieved_text, re.IGNORECASE))
        color = "#ffb000" if is_active else "#555555"
        weight = "bold" if is_active else "normal"
        glow = "text-shadow: 0 0 10px #ffb000;" if is_active else ""
        
        timeline_html += f"<div style='color: {color}; font-weight: {weight}; {glow} font-family: Share Tech Mono;'>{data['label']}</div>"
    
    timeline_html += "</div>"
    st.markdown(timeline_html, unsafe_allow_html=True)

# Main UI
st.title("Librarius Omnis")
st.markdown("*Seek the truth of the Imperium.*")

user_query = st.text_input("Enter Query Directive:", value=selected_question, key="main_user_query")

if st.button("Execute Query", key="btn_execute_query"):
    if user_query:
        try:
            # Step 1: Retrieval
            with st.spinner("Accessing Qdrant Databanks..."):
                retrieved_chunks = retriever.retrieve(user_query, top_k=3)
                full_context = " ".join([c["text"] for c in retrieved_chunks])
                
                render_timeline(full_context)
                
                st.markdown("### Process Telemetry")
                col1, col2, col3 = st.columns(3)
                col1.metric("Engine", "BGE-M3 (CPU)")
                col2.metric("Top-K Hits", len(retrieved_chunks))
                col3.metric("Max Confidence", f"{retrieved_chunks[0]['score']:.4f}" if retrieved_chunks else "0.0")
                
                with st.expander("View Retrieved Source Documents"):
                    for idx, chunk in enumerate(retrieved_chunks):
                        st.markdown(f"**Source:** `{chunk['source']}` | **Score:** `{chunk['score']}`")
                        st.info(chunk["text"])

            # Step 2: Generation
            with st.spinner("Synthesizing answer via Qwen2.5-3B..."):
                answer = generator.generate_answer(user_query, retrieved_chunks)
                
                st.markdown("---")
                st.markdown("### Imperial Scholar Response")
                st.write(answer)

        except Exception as e:
            st.error(f"Execution Error Encountered: {str(e)}")
            st.exception(e)
    else:
        st.warning("Please enter a query.")