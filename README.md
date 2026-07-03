# 🤖 LangChain Study & Chatbot Workspace

Welcome to my **LangChain & GenAI Study Workspace**! This repository serves as a structured environment for learning, experimenting, and building applications with **LangChain (v1.x)**, **Google Gemini**, and other LLM ecosystems.

It currently features a fully decoupled, production-grade Streamlit Chatbot integrated with **LangSmith Observability**, plus various scratch scripts and design planners.

---

## 📂 Repository Structure

The workspace is organized as follows:

```text
LangChain/
├── .env                                  # Local environment variables (API Keys, tracing configs)
├── .gitignore                            # Git exclusion patterns
├── requrements.txt                       # Project dependencies
├── README.md                             # Parent/workspace documentation (This file)
│
├── Documents/                            # Learning path planners and study guides
│   └── LangChain & GenAI Learning Planner.docx
│
└── LangChain_ChatBot/                    # Main application directory
    ├── app.py                            # Streamlit frontend application entry point
    ├── openai_app.py                     # OpenAI-based chatbot prototype
    ├── readme.md                         # Chatbot-specific architecture & detailed guide
    └── src/                              # Modular business logic
        ├── chain.py                      # Composition of LangChain components (LCEL)
        ├── history.py                    # Session state and chat history management
        ├── langsmith_config.py           # Synchronous LangSmith tracing & validation setup
        ├── llm.py                        # Model initialization (Gemini 2.5 Flash)
        └── prompts.py                    # Structured prompt template definitions
```

---

## 🛠️ Technology Stack

- **Orchestration:** LangChain (v1.x)
- **Primary LLM:** Google Gemini 2.5 Flash (`gemini-2.5-flash` via `langchain-google-genai`)
- **Observability:** LangSmith (for full-trace request debugging, latency analysis, and cost tracking)
- **Frontend UI:** Streamlit
- **Environment Management:** `python-dotenv` & Python `venv`

---

## 🚀 Getting Started

### 1. Prerequisite: Setup Environment variables
Create a `.env` file in the **root** workspace directory and configure your credentials:

```env
# Google Gemini API Key
Google_API_KEY='YOUR_GOOGLE_GEMINI_API_KEY'

# LangSmith Tracing Configuration
LANGCHAIN_API_KEY='YOUR_LANGSMITH_API_KEY'
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT='Learning'
```

> [!NOTE]
> Ensure your API keys are wrapped in single or double quotes, and do not commit the `.env` file to your version control.

### 2. Install & Run
Run the following commands in your terminal:

```powershell
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install required packages
pip install -r requrements.txt

# 4. Launch the Streamlit application
streamlit run .\LangChain_ChatBot\app.py
```

---

## 🧠 Architecture & Architectural Patterns Learned

This workspace applies modern software engineering principles to generative AI:

1. **Separation of Concerns:** The Streamlit frontend ([app.py](file:///c:/Sourav/Study/FDE/Study/LangChain/LangChain_ChatBot/app.py)) acts strictly as a visual layer. All core business logic—including prompting, model definition, memory management, and pipeline orchestration—lives in the standalone `src/` directory.
2. **Stateless LLMs & Chat History:** Since models are stateless, conversation history is preserved across runs. This is achieved using `RunnableWithMessageHistory` and `InMemoryChatMessageHistory` from the LangChain framework.
3. **Synchronous LangSmith Credentials Verification:** In [langsmith_config.py](file:///c:/Sourav/Study/FDE/Study/LangChain/LangChain_ChatBot/src/langsmith_config.py), we check the validity of your LangSmith credentials at startup. If the credentials fail or are expired (HTTP `403 Forbidden`), tracing is disabled automatically, and a user-friendly UI warning is shown instead of failing silently or polluting console output.
4. **LangChain Expression Language (LCEL):** Pipelines are defined declaratively using the pipe (`|`) operator:
   ```python
   chain = prompt | llm | parser
   ```

---

## 🗺️ Roadmap & Next Steps

This repository will evolve to cover advanced GenAI patterns:
* **Retrieval-Augmented Generation (RAG):** Document loading, text splitting, embedding creation, and semantic searching using vector databases (FAISS, Chroma).
* **Multi-Chat Sessions:** UI updates to support multiple parallel conversation streams.
* **Structured Output Parsing:** Enforcing JSON outputs from models for reliable programmatic integration.
* **AI Agents & Tool Calling:** Empowering models to invoke local scripts and external APIs.
* **LangGraph:** Creating complex, stateful multi-agent workflows.
