# Librarius Omnis — Domain-Specific Local RAG System

**Librarius Omnis** is a privacy-first, 100% offline Retrieval-Augmented Generation (RAG) system engineered to process, index, and query dense Warhammer 40,000 lore. Built for local execution on consumer-grade hardware, it pairs a custom Streamlit imperial cogitator terminal with a Dockerized Qdrant vector database and host GPU acceleration via Ollama.

---

## Technical Architecture

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                                OFFLINE INGESTION                                  │
│                                                                                   │
│  [Raw Documents] ──► [Cleaner & Chunker] ──► [Chunks] ──► (1) BGE-M3 (CPU/CUDA)   │
│                                                                 │                 │
│                                                                 ▼                 │
│  [Qdrant Docker Volume] ◄───────────────────────────── (2) Index via HTTP (6333)  │
└───────────────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                            ONLINE RETRIEVAL & STREAMLIT                           │
│                                                                                   │
│  User Input (Streamlit UI) ──► (3) BGE-M3 Embedder ──► (4) Qdrant Vector Search   │
│                                                                 │                 │
│                                                                 ▼                 │
│  Output Display ◄── (7) Response ◄── Ollama Qwen2.5 ◄── (5) Top-K Chunks + Context │
│  & Timeline Sync     (Host GPU)      (host.docker.internal)                       │
└───────────────────────────────────────────────────────────────────────────────────┘

```

---

## Key Features

* **Interactive Imperial Web Interface:** Styled Streamlit dashboard ("Librarius Omnis") featuring background art randomization, telemetry metric boxes, source document inspect expanders, and dynamic lore timeline parsing (M30–M42).
* **Multi-Container Architecture:** Completely containerized using Docker Compose (`rag-app` and `qdrant`), decoupling local storage dependencies from host OS lock files.
* **Host GPU Acceleration:** Uses Docker `host-gateway` bridge (`host.docker.internal`) to route LLM inference calls directly to host-level GPU-accelerated Ollama instances.
* **Native Thread Safety:** Enforces single-threaded OpenMP/MKL constraints at application entry to prevent Windows native C++ matrix math crashes (`0xC0000005` access violations) during PyTorch initialization.
* **100% Offline & Private:** Zero cloud API dependencies; embeddings, vectors, and generation execute completely locally.

---

## Environment Variables & Configuration

The application dynamically detects its deployment environment using the following variables:

| Variable | Default Value | Description |
| --- | --- | --- |
| `QDRANT_HOST` | `localhost` | Hostname/IP of the Qdrant service (`qdrant` inside Docker) |
| `QDRANT_PORT` | `6333` | HTTP port for the Qdrant vector database |
| `OLLAMA_HOST` | `http://localhost:11434` | Endpoint for the Ollama inference engine (`[http://host.docker.internal:11434](http://host.docker.internal:11434)` in Docker) |
| `OMP_NUM_THREADS` | `1` | OpenMP thread limit (prevents C++ worker thread collisions) |
| `TOKENIZERS_PARALLELISM` | `false` | Disables Hugging Face tokenizer thread parallelism |

---

## Project Structure

```text
├── assets/
│   └── backgrounds/        # Visual assets and background images for Streamlit UI
├── data/
│   ├── raw/                # Raw source text files (.txt)
│   └── processed/          # Generated chunks.json artifact
├── evals/                  # Benchmark dataset (80 structured evaluation questions)
│   ├── questions.json
│   ├── questions.txt
│   └── questions/          # Category-specific evaluation subsets
├── src/
│   ├── embeddings/         # BGE-M3 embedding wrapper
│   ├── retrieval/          # LoreRetriever (Qdrant client integration)
│   └── generation/         # LoreGenerator (Ollama client integration)
├── app.py                  # Main Streamlit web application & UI orchestrator
├── build_index.py          # Vector database ingestion pipeline script
├── Dockerfile              # Container definition for Streamlit RAG application
├── docker-compose.yml      # Orchestration for Qdrant and RAG application services
├── .dockerignore           # Excludes heavy local venvs and build caches from Docker context
├── Modelfile               # Ollama custom model definition file
├── requirements.txt        # Python dependency manifest
└── README.md               # Project documentation

```

---

## Data Pipeline & Ingestion

1. **Preprocessing:** Strips control characters, normalizes line breaks, and enforces structural boundaries across over 1.8M characters of raw lore text.
2. **Sliding Window Chunking:** Divides documents into **2,762 chunks** with an 800-character window and a 150-character overlap to preserve entity names and semantic context.
3. **HTTP Vector Indexing:** Batch-embeds text chunks using `BAAI/bge-m3` and persists 1024-dimensional vectors directly into the Qdrant instance via HTTP payload.

---

## Evaluation Benchmark Suite (`evals/`)

The repository includes an evaluation benchmark designed to measure retrieval precision and generation fidelity across four query categories:

### Query Breakdown

* **Basic:** Standard, single-entity lore retrieval questions.
* **Multi-hop:** Complex queries requiring context synthesis across multiple documents.
* **Adversarial:** Misleading questions with false premises to test hallucination resistance.
* **Chronology:** Timeline questions testing historical sequences (e.g., Great Crusade vs. Era Indomitus).

---

## Quick Start

### Option A: Deployment via Docker Compose (Recommended)

#### 1. Configure Host Ollama

Ensure local Ollama accepts requests from Docker containers. In Windows PowerShell:

```powershell
$env:OLLAMA_ORIGINS="*"
ollama serve

```

Ensure your desired local model is pulled:

```powershell
ollama pull qwen2.5:3b

```

#### 2. Launch Stack via Docker Compose

From the repository root, start both the `qdrant` vector database and `rag-app` containers:

```bash
docker compose up --build -d

```

#### 3. Populate Vector Database (First Time Only)

Run the ingestion pipeline inside the running application container:

```bash
docker compose exec rag-app python build_index.py

```

#### 4. Access Terminal Interface

Open your browser and navigate to `http://localhost:8501`.

---

### Option B: Local Development Setup (Native Python)

#### 1. Prerequisites

* Python 3.10+
* Local [Qdrant Container](https://hub.docker.com/r/qdrant/qdrant) running on port `6333`
* [Ollama](https://ollama.ai/) running locally

#### 2. Installation

```bash
# Clone repository
git clone https://github.com/your-username/librarius-omnis-rag.git
cd librarius-omnis-rag

# Setup virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

#### 3. Build Vector Index

Ensure Qdrant is running (`docker run -p 6333:6333 qdrant/qdrant`), then execute:

```bash
python build_index.py

```

#### 4. Run Streamlit App

```bash
streamlit run app.py

```