# Retrieval-Augmented Generation (RAG) Pipeline

This directory contains a complete, self-contained implementation of a **Retrieval-Augmented Generation (RAG)** pipeline built using LangChain, Google Gemini Embeddings, and FAISS. 

The pipeline ingests multi-source data (text, PDF, and web pages), splits and indexes it into a local vector database, and performs similarity searches to retrieve contextually relevant passages.

---

## Directory Structure

```
RAG/
├── Data/
│   ├── attention.pdf      # "Attention Is All You Need" research paper
│   ├── Speech.txt         # Swami Vivekananda's Parliament of Religions speech
│   └── data.txt           # Miscellaneous unstructured text data
├── SimpleRAG.ipynb        # Core Jupyter Notebook implementing the RAG pipeline
└── README.md              # Project documentation (this file)
```

---

## Technical Stack & Libraries

The RAG pipeline is implemented in Python and leverages the following key frameworks:

- **Orchestration**: `langchain` & `langchain-community`
- **LLM & Embeddings Provider**: `langchain-google-genai` (utilizing Google Generative AI)
- **Vector Database**: `faiss-cpu` (Facebook AI Similarity Search)
- **Document Parsers**: `pypdf` (for PDF files) and `beautifulsoup4` (for web content loaders)
- **Environment Management**: `python-dotenv`

---

## Key Pipeline Steps

### 1. Multi-Source Data Ingestion
The pipeline processes three different types of document sources:
- **Text Loader**: Ingests `Data/Speech.txt` using `TextLoader`.
- **PDF Loader**: Ingests the Transformer research paper (`Data/attention.pdf`) using `PyPDFLoader`.
- **Web Loader**: Scrapes and parses Lilian Weng's blog post on LLM Powered Autonomous Agents using `WebBaseLoader`.

### 2. Document Chunking
To fit context windows and improve retrieval granularity, documents are split into smaller chunks using the `RecursiveCharacterTextSplitter`:
- **Chunk Size**: `1000` characters
- **Chunk Overlap**: `200` characters

### 3. Vector Embeddings & Indexing
- **Embeddings Model**: `gemini-embedding-2-preview` (configured via `GoogleGenerativeAIEmbeddings`)
- **Vector Database**: **FAISS** index built locally from the chunked documents.

### 4. Similarity Search & Retrieval
Executes semantic queries against the index to return the most relevant document chunks based on cosine similarity.

---

## Setup & Execution

### Prerequisites

Ensure you have a `.env` file in your root workspace directory containing your Google API key:

```env
Google_API_KEY="your_google_gemini_api_key_here"
```

### Installation

Install the required dependencies from the root repository:

```bash
pip install -r ../requrements.txt
```

*(Alternatively, run the inline installation command inside the notebook).*

### Running the Notebook

Start Jupyter Notebook or open `SimpleRAG.ipynb` in VS Code / Jupyter Lab and execute the cells sequentially to build the vector store and run similarity search queries.
