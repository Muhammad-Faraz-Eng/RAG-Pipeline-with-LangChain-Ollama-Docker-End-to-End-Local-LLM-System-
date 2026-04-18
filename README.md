# 🚀 RAG Pipeline with LangChain, Ollama & Docker

## 📌 Overview

This project implements an **end-to-end Retrieval-Augmented Generation (RAG) system** using:

* Python
* LangChain
* Docker & Docker Compose
* Local LLM (Ollama)
* Vector search (ChromaDB)
* HuggingFace embeddings

The system retrieves relevant context from input data and generates answers using a **fully local LLM**, avoiding external APIs like OpenAI.

---

## 🎯 Key Features

* 🔍 Semantic search using embeddings
* 🧩 Intelligent text chunking with overlap
* 📦 Vector storage using ChromaDB
* 🤖 Local LLM inference using Ollama
* 🔗 End-to-end RAG pipeline (Retrieval + Generation)
* 🐳 Fully containerized with Docker
* ⚡ Fast dependency management using `uv`

---

## 🧠 Architecture

```
Document
   ↓
Chunking (Text Splitter)
   ↓
Embeddings (HuggingFace)
   ↓
Vector Store (ChromaDB)
   ↓
Retriever (Top-K Similarity Search)
   ↓
LLM (Ollama - TinyLlama)
   ↓
Final Answer
```

---

## 🛠️ Tech Stack

| Component        | Tool Used             |
| ---------------- | --------------------- |
| Language         | Python                |
| LLM Runtime      | Ollama                |
| Framework        | LangChain             |
| Vector Store     | ChromaDB              |
| Embeddings       | Sentence Transformers |
| Containerization | Docker + Compose      |
| Package Manager  | uv                    |

---

## 📂 Project Structure

```
rag-project/
├── app/
│   ├── main.py              # Full RAG pipeline
│   ├── retrieval.py         # Manual retrieval logic (learning phase)
│   ├── llm.py               # Ollama integration
│   └── langchain_rag.py     # LangChain implementation
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
├── README.md
```

---

## ⚙️ Setup & Run

### 1️⃣ Build & Start Containers

```bash
docker-compose up --build
```

---

### 2️⃣ Pull LLM Model (First Time Only)

```bash
docker exec -it ollama ollama pull tinyllama
```

---

### 3️⃣ Restart App

```bash
docker-compose restart app
```

---

## 💡 Example Query

```text
Query: Who is admin?
```

### ✅ Output

```text
Faraz is the admin.
```

---

## 🔬 Learning Highlights

This project was built in two stages:

### 🧩 Phase 1 — Manual RAG Implementation

* Built chunking logic from scratch
* Implemented cosine similarity
* Designed Top-K retrieval
* Understood embedding behavior

### 🔗 Phase 2 — LangChain Integration

* Abstracted pipeline using LangChain
* Used built-in retriever and chains
* Integrated vector store and LLM seamlessly

---

## ⚠️ Key Insights

* Retrieval quality directly impacts LLM output
* Chunking strategy is critical for accuracy
* LLM does not verify truth — it relies on provided context
* Poor retrieval leads to hallucinations or misleading answers

---

## 🚧 Limitations

* No re-ranking or filtering of retrieved chunks
* Basic prompt engineering
* No persistent external vector database (Chroma is in-memory)

---

## 🔮 Future Improvements

* Add re-ranking layer for better retrieval
* Implement metadata filtering
* Integrate Airflow for orchestration
* Use hybrid search (keyword + vector)
* Add API layer (FastAPI)

---

## 📈 Resume Value

This project demonstrates:

* Strong understanding of RAG architecture
* Hands-on experience with LangChain
* LLM integration without external APIs
* Docker-based production-ready setup
* Data engineering mindset (pipelines, processing, retrieval)

---

## 👤 Author

**Muhammad Faraz Eng**
Aspiring Data Engineer

---

## ⭐ If you found this useful, consider starring the repo!
