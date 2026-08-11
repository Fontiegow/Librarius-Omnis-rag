Here is a structured, production-ready `README.md` file tailored for your repository. It incorporates the complete technical architecture from your report along with the evaluation dataset breakdown you provided.

---

# Librarius Omnis — Domain-Specific Local RAG System

**Librarius Omnis** is a privacy-first, 100% offline Retrieval-Augmented Generation (RAG) system engineered to process, index, and query dense Warhammer 40,000 lore. Built to run locally on consumer-grade hardware with strict memory constraints, it leverages GPU acceleration for embeddings and local LLM execution via Ollama.

---

## Technical Architecture

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                               OFFLINE INGESTION                                   │
│                                                                                   │
│  [Raw Documents] ──► [Cleaner & Chunker] ──► [Chunks] ──► (1) BGE-M3 (GPU)        │
│                                                                  │                │
│                                                                  ▼                │
│  [qdrant_db/ Storage] ◄─────────────────────────────── (2) Index in Qdrant Vector DB
└───────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                               ONLINE RETRIEVAL                                    │
│                                                                                   │
│  User Query ─────────► (3) BGE-M3 (GPU) ──► (4) Cosine Similarity Search in Qdrant│
│                                                                  │                │
│                                                                  ▼                │
│  Response ◄── (7) Output ◄── (6) Prompt ◄── Ollama Qwen2.5 ◄── (5) Relevant Chunks│
└───────────────────────────────────────────────────────────────────────────────────┘

```

---

## Key Features

* **100% Offline & Private:** Zero cloud dependencies; all vectors and LLM inferences execute locally.
* **Low VRAM Optimization:** Tailored for consumer GPUs (e.g., RTX 3050 4GB VRAM) using 4-bit quantized local models.
* **Dense Semantic Embeddings:** Uses `BAAI/bge-m3` running on CUDA to map lore text into 1024-dimensional vectors.
* **Embedded Vector Database:** Disk-persisted local Qdrant collection with Cosine similarity indexing.
* **Grounded Generation:** Enforces strict context grounding with low temperature ($0.2$) via Ollama's `Qwen2.5-3B-Instruct`.

---

## Data Pipeline & Ingestion

1. **Preprocessing:** Strips control characters, normalizes line breaks, and enforces paragraph boundaries across over 1.8M characters of raw lore text.
2. **Sliding Window Chunking:** Divides documents into **2,762 chunks** with an 800-character window and a 150-character overlap to preserve entity names and semantic continuity across boundaries.
3. **Vector Indexing:** Batch-embeds text chunks onto local GPU memory and persists them inside `./qdrant_db/` along with metadata payloads.

---

## Evaluation Benchmark Suite (`evals/`)

The repository includes a benchmark dataset designed to evaluate retrieval precision and generation fidelity across various query types.

### Dataset Overview

* **Total Evaluation Questions:** 80
* **Structure:** Each item in the dataset contains:
* `id`: Unique identifier
* `question`: The input evaluation query
* `ground_truthanswer`: The verified reference answer
* `key_facts`: Crucial lore facts required for a correct answer
* `metadatacategory`: Category classification
* `difficulty`: Metric difficulty rating
* `question_type`: Query structure classification
* `retrieval_hops`: Number of document contexts required to answer
* `contains_false_premise`: Boolean flag for trick/adversarial questions



### Query Categories

* **Basic:** Standard, straightforward lore retrieval questions.
* **Multi-hop:** Complex queries requiring context assembly from multiple lore documents.
* **Adversarial:** Questions containing misleading assumptions or false premises to test hallucination resistance.
* **Chronology:** Temporal questions testing historical timelines and event sequences.

### File Structure (`evals/`)

```text
evals/
├── questions.json      # Complete dataset with full metadata schemas
├── questions.txt       # Plain text list of raw evaluation queries
└── questions/          # Directory containing category-specific subsets

```

---

## Quick Start

### 1. Prerequisites

* Python 3.10+
* CUDA-compatible GPU (NVIDIA RTX 3050 or higher recommended)
* [Ollama](https://ollama.ai/) installed locally

### 2. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/librarius-omnis-rag.git
cd librarius-omnis-rag

# Activate your virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install PyTorch with CUDA support and dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install qdrant-client sentence-transformers ollama huggingface_hub

```

### 3. Register local LLM model in Ollama

If using a custom downloaded GGUF file:

```bash
ollama create qwen2.5:3b -f Modelfile

```

### 4. Build Vector Index

Process raw data and generate local Qdrant vectors:

```bash
python build_index.py

```

### 5. Run RAG Engine

Launch the interactive command-line interface:

```bash
python main_rag.py

```

---

## Project Structure

```text
├── data/
│   ├── raw/               # 10 raw lore source text files
│   └── processed/         # Generated chunks.json artifact
├── evals/                 # Benchmark dataset (80 structured questions)
├── src/
│   ├── embeddings/        # BGE-M3 CUDA embedding wrapper
│   ├── retrieval/         # Qdrant search and retrieval logic
│   └── generation/        # Ollama prompt builder and generator
├── build_index.py         # Offline vector database ingestion pipeline
├── main_rag.py            # Main interactive RAG CLI orchestrator
├── Modelfile              # Ollama model definition file
└── README.md              # Project documentation

```# Librarius-Omnis-rag
