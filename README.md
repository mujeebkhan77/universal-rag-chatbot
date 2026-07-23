# Universal RAG Chatbot 🤖

A full-stack AI-powered document assistant that allows users to upload documents, add YouTube videos, and ask questions using Retrieval-Augmented Generation (RAG).

The application retrieves relevant information from uploaded sources and generates accurate answers with source references.

---

## 🚀 Features

- Upload PDF documents
- Upload TXT files
- Upload DOCX files
- Add YouTube videos using URL
- Ask questions about uploaded content
- AI-generated answers using RAG pipeline
- Source references for answers
- Document management:
  - View uploaded documents
  - Delete documents
- Vector-based semantic search
- Modern React user interface

---

## 🏗️ Architecture

The application follows a client-server architecture.

```
User
 |
 |
React Frontend
(Vite + Tailwind CSS)
 |
 |
FastAPI Backend
 |
 |
LangChain RAG Pipeline
 |
 |
ChromaDB Vector Database
 |
 |
LLM + Embeddings
```

---

# 🛠️ Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- Lucide React Icons

## Backend

- Python
- FastAPI
- LangChain

## AI / RAG

- Retrieval-Augmented Generation (RAG)
- HuggingFace Embeddings
- ChromaDB Vector Store
- Gemini Flash LLM

## Document Processing

- PDF Loader
- DOCX Loader
- TXT Loader
- YouTube Transcript Loader

---

# 📂 Project Structure

```
Universal-RAG-Chatbot

│
├── backend
│   │
│   ├── main.py
│   ├── requirements.txt
│   │
│   └── src
│       │
│       ├── ingestion.py
│       ├── embeddings.py
│       ├── vectorstore.py
│       ├── splitter.py
│       │
│       └── loaders
│           ├── pdf_loader.py
│           ├── docx_loader.py
│           ├── txt_loader.py
│           └── youtube_loader.py
│
│
└── frontend
    │
    ├── src
    │   │
    │   ├── App.jsx
    │   ├── components
    │   │   ├── Sidebar.jsx
    │   │   ├── ChatWindow.jsx
    │   │   ├── Message.jsx
    │   │   └── InputBox.jsx
    │   │
    │   └── api
    │       └── client.js
    │
    ├── package.json
    └── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```
git clone (https://github.com/mujeebkhan77/universal-rag-chatbot)

cd Universal-RAG-Chatbot
```

---

# Backend Setup

Move into backend:

```
cd backend
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run backend:

```
uvicorn main:app --reload
```

Backend will run at:

```
http://localhost:8000
```

---

# Frontend Setup

Open another terminal:

```
cd frontend
```

Install dependencies:

```
npm install
```

Start development server:

```
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

# 🔄 How It Works

## 1. Document Upload

User uploads:

- PDF
- DOCX
- TXT
- YouTube video


The backend:

1. Extracts text
2. Splits text into chunks
3. Generates embeddings
4. Stores vectors in ChromaDB


---

## 2. Question Answering

When a user asks a question:

1. Query is converted into embeddings
2. Similar documents are retrieved
3. Relevant context is passed to the LLM
4. AI generates an answer
5. Sources are returned to the user


---

# Example Workflow

```
Upload PDF
      |
      ↓
Text Extraction
      |
      ↓
Chunking
      |
      ↓
Embeddings
      |
      ↓
ChromaDB Storage
      |
      ↓
User Question
      |
      ↓
Retriever
      |
      ↓
LLM Answer
      |
      ↓
Response + Sources
```

---

# Environment Variables

Create a `.env` file inside backend:

```
GOOGLE_API_KEY=your_api_key_here
```

---

# Future Improvements

Possible improvements:

- Authentication system
- Cloud storage for documents
- Streaming AI responses
- Better retrieval algorithms
- Conversation memory
- Multiple user workspaces
- Production database integration
- Deployment with Docker

---

# 🎯 Project Goal

The goal of this project is to build a practical AI assistant that can understand private user documents and answer questions using Retrieval-Augmented Generation instead of relying only on general AI knowledge.

---

# Author

Built by **Majeeb Ullah**

Software Engineering Student

AI / LLM Application Developer
