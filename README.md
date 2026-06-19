
🧠 Lightweight RAG System 
-------
Retrieval-Augmented Generation – 100% local, no API calls, runs on      minimal hardware!

https://img.shields.io/badge/Python-3.8+-blue https://img.shields.io/badge/ChromaDB-0.5+-green

https://img.shields.io/badge/Transformers-4.30+-orange 

https://img.shields.io/badge/License-MIT-yellow

✨ Highlights

    🚀 No API keys – everything runs locally
    
    💾 Tiny model – flan-t5-small (only 300 MB, ~1–2 GB RAM)
    
    🔍 Semantic search with ChromaDB & Sentence‑Transformers
    
    📄 Supports PDF & TXT files
    
    ⚡ Quick setup – just clone, install, and run
    
    🎯 Perfect for learning RAG without expensive hardware

📁 Project Structure

  rag-system/
  
    ├── src/
    
    │   ├── config.py          # Configuration (no API keys needed)
    
    │   ├── ingest.py          # Load & chunk documents
    
    │   ├── embed_store.py     # Embeddings & ChromaDB storage
    
    │   ├── retrieval.py       # Retrieve relevant chunks
    
    │   ├── generate.py        # Generate answers with flan-t5-small
    
    │   └── main.py            # Main pipeline
    
    ├── data/                  # Put your .txt / .pdf files here  
    
    ├── chroma_db/             # Vector database (auto‑created)
    
    ├── .env                   # Optional (not required)
    
    ├── requirements.txt
    
    └── README.md

🛠️ Requirements
---
    Python 3.8+
    RAM: ~2 GB (or more for large documents)
    Storage: ~1 GB (for model cache + DB)
    No GPU required – runs fine on CPU

🚀 Quick Start
-  
  1️⃣ Clone & Enter
  
    git clone https://github.com/yourusername/rag-system.git
    cd rag-system
  2️⃣ Create a Virtual Environment
  
    python -m venv venv
    source venv/bin/activate      # Linux/macOS
    # or
    venv\Scripts\activate         # Windows
  3️⃣ Install Dependencies
  
    pip install -r requirements.txt
  4️⃣ Add Your Documents
  
    Put any .txt or .pdf files into the data/ folder:
    mkdir -p data
    echo "Your document content..." > data/sample.txt
  5️⃣ Run the System
  
    python src/main.py
  That’s it! Start asking questions about your documents.
  
💬 Example Interaction
-
  🤖 Starting RAG System...  
  📄 Loading documents...  
  ✅ Loaded TXT: sample.txt
  📊 Created 48 chunks
  
  💾 Building vector database...
  💾 Stored 48 chunks
  
  ✅ RAG System Ready!
  --------------------------------------------------

  ❓ Your question: What is DeepSeek?

  🔍 Searching...
  🧠 Generating answer...

-
  📝 Answer: DeepSeek is an AI company that develops
  advanced language models for chat, coding, and reasoning.
-

⚙️ Configuration
-
  Change Chunk Size
  In src/ingest.py:
  
      def chunk_texts(texts, chunk_size=500, chunk_overlap=50):
      //Increase chunk_size for larger context
  Switch to a Bigger Model (if you have more RAM)
    In src/generate.py:
    
    generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",   # or "google/flan-t5-large")
  Adjust Retrieval Top‑K
    In src/retrieval.py:
    
      def retrieve(query, collection, top_k=5):
    # Increase top_k for more context chunks
    
📦 Dependencies
-
  chromadb>=0.5.0
  sentence-transformers>=2.2.0
  pypdf>=4.0.0
  python-dotenv>=1.0.0
  transformers>=4.30.0
  torch>=2.0.0
  All are listed in requirements.txt.

  🧠 How It Works (Simplified)
  -
  1.Ingest – load and split documents into chunks.
  
  2.Embed – convert each chunk into a vector using all-MiniLM-L6-v2.
  
  3.Store – save vectors in ChromaDB (persistent on disk).
  
  4.Retrieve – for a query, find the most similar chunks.
  
  5.Generate – feed the retrieved context to flan-t5-small to produce an answer.
  
  All steps run locally – no data leaves your machine.

## 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| `FileNotFoundError: data` | Create the `data/` folder manually with `mkdir data` |
| `Out of Memory` | Use `flan-t5-small` (already default) or reduce `chunk_size` in `ingest.py` |
| `ModuleNotFoundError: No module named 'X'` | Run `pip install -r requirements.txt` again |
| `AttributeError: 'Document' object has no attribute 'get'` | Use the dictionary-based version of `ingest.py` (provided in the repo) |
| `Error code: 402 - Insufficient Balance` | Use the local Tiny Model (no API key needed) or add credits to your DeepSeek account |
| `git push` asks for password | Use a **Personal Access Token** (not your GitHub password) |
| `fatal: remote origin already exists` | Run `git remote set-url origin NEW_URL` to update the remote URL |
| `You have uncommitted changes` | Run `git add .` and `git commit -m "message"` again |
| Slow performance | - Use `flan-t5-small` (lightest model) <br> - Reduce `chunk_size` in `ingest.py` <br> - Run on CPU with `device=-1` (default) |
| HF_TOKEN warning | Ignore it – the model works without a token (limited rate only) |
| ChromaDB: `Expected metadata to be a non-empty dict` | Make sure each chunk has a `metadata` dictionary with at least one key (e.g., `source`) |
| `Permission denied` when pushing to GitHub | Use a **Personal Access Token** with `repo` scope instead of your password |

##🤝 Contributing
    Fork the repo.
    Create a feature branch.
    Make your changes.
    Open a Pull Request.
    
##🧩 Future Improvements
    Support for more file types (DOCX, HTML)
    Web UI (Streamlit/Gradio)
    Add evaluation metrics
    Streaming responses
-
Made with ❤️ for the open‑source community.
-
  
