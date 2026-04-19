# 🧠 Knowledge Graph RAG vs Traditional RAG (Physics - Grade 9)

## 🚀 Overview

This project implements a **Knowledge Graph-based Retrieval-Augmented Generation (KG-RAG)** system and compares it with traditional RAG.

It uses:

* **Neo4j** for knowledge graph storage
* **LLM (OpenAI)** for reasoning
* **FAISS + embeddings** for traditional RAG
* **Streamlit** for interactive UI

---

## 🎯 Key Features

* 🔗 Auto-build Knowledge Graph from PDF
* 🧠 Multi-hop reasoning using graph relationships
* 📄 Traditional RAG using semantic search
* ⚔️ KG-RAG vs Traditional RAG comparison
* 📊 Metrics: Cosine, BLEU, ROUGE
* 🎯 Confidence scoring
* 🌐 Graph visualization

---

## 🧠 Architecture

See detailed architecture: [`docs/architecture.md`](docs/architecture.md)

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/your-username/kg-rag-physics.git
cd kg-rag-physics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

```bash
cp .env.example .env
```

Fill your API keys.

---

### 4. Run Neo4j

Install and start Neo4j locally.

---

### 5. Run App

```bash
streamlit run app.py
```

---

## 📊 Example Workflow

1. Upload NCERT Physics PDF
2. Build Knowledge Graph
3. Ask questions
4. Compare KG-RAG vs Traditional RAG
5. View metrics + graph reasoning

---

## 🧪 Evaluation Metrics

* Cosine Similarity
* BLEU Score
* ROUGE Score

---

## 📈 Results

See: [`docs/results.md`](docs/results.md)

---

## 🧠 Why Knowledge Graph RAG?

| Feature              | Traditional RAG | KG-RAG |
| -------------------- | --------------- | ------ |
| Explainability       | ❌               | ✅      |
| Multi-hop reasoning  | ❌               | ✅      |
| Structured knowledge | ❌               | ✅      |

---

## 💡 Future Work

* Improved entity extraction
* Graph pruning
* Domain-specific ontology
* Multi-modal support

---

## 📜 License

MIT License
