# 🤖 LangChain Chatbot with Google Gemini

## 📖 Project Overview

This project is my first hands-on implementation of **LangChain** using the latest LangChain architecture (v1.x), **Google Gemini**, **Streamlit**, and **LangSmith**.

The objective of this project was not only to build a chatbot but also to understand the architecture behind modern LLM applications.

This project serves as the foundation for future enhancements such as Retrieval-Augmented Generation (RAG), AI Agents, Tool Calling, Vector Databases, and LangGraph.

---

# 🚀 Technologies Used

* Python 3.x
* Streamlit
* LangChain (v1.x)
* Google Gemini 2.5 Flash
* LangSmith
* python-dotenv

---

# 📂 Project Structure

```
LangChain_ChatBot/

│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
└── src/
      ├── llm.py
      ├── prompts.py
      ├── history.py
      └── chain.py
```

---

# 🏗️ Application Architecture

```
                User
                  │
                  ▼
          Streamlit Chat UI
                  │
                  ▼
     RunnableWithMessageHistory
                  │
                  ▼
          Prompt Template
                  │
                  ▼
      ChatGoogleGenerativeAI
                  │
                  ▼
          Gemini 2.5 Flash
                  │
                  ▼
          Output Parser
                  │
                  ▼
             AI Response

                  ▲
                  │
          LangSmith Tracing
```

---

# 📚 What I Learned

## 1. LangChain is NOT an LLM

LangChain is an orchestration framework.

Gemini generates text.

LangChain manages:

* Prompt Templates
* Chat History
* Chains
* Output Parsing
* Tools
* Agents
* RAG Pipelines

---

## 2. Separation of Concerns

Instead of writing everything inside one file, responsibilities were separated.

### app.py

Responsible only for the Streamlit User Interface.

### llm.py

Responsible for creating the Gemini model.

### prompts.py

Contains Prompt Templates.

### history.py

Maintains conversation history.

### chain.py

Connects all components into a runnable LangChain pipeline.

---

## 3. Prompt Templates

Instead of directly sending user input to Gemini, LangChain builds a structured prompt containing:

* System Prompt
* Previous Conversation
* Current User Question

This provides better control over model behaviour.

---

## 4. Chat History

Large Language Models are **stateless**.

They do not remember previous API calls.

Conversation history is maintained by LangChain and injected into the prompt before every request.

Modern LangChain uses:

* RunnableWithMessageHistory
* InMemoryChatMessageHistory

instead of the older memory classes.

---

## 5. Streamlit Session State

Streamlit reruns the entire script after every interaction.

To preserve conversation on the UI, chat messages are stored inside:

```
st.session_state
```

Without session state, every rerun would clear the conversation.

---

## 6. LangChain Expression Language (LCEL)

The chain is built using the pipe operator.

```
Prompt
    │
    ▼
LLM
    │
    ▼
Output Parser
```

Example:

```python
chain = prompt | llm | parser
```

This creates a clean and readable execution pipeline.

---

## 7. RunnableWithMessageHistory

This is the modern conversation memory implementation introduced in LangChain.

It automatically:

* Loads previous messages
* Injects history into the prompt
* Sends the request to the model
* Saves the latest interaction

No manual memory management is required.

---

## 8. LangSmith

LangSmith provides observability for LangChain applications.

Every invocation records:

* Prompt
* Chat History
* Model Response
* Execution Time
* Latency
* Token Usage (when supported)
* Errors

This makes debugging and optimisation significantly easier.

---

# ⚙️ Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

LANGCHAIN_API_KEY=YOUR_LANGSMITH_API_KEY

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=Learning
```

---

# ▶️ Running the Application

Create a virtual environment.

```
python -m venv venv
```

Activate it.

Windows

```
venv\Scripts\activate
```

Install dependencies.

```
pip install -r requirements.txt
```

Run Streamlit.

```
streamlit run app.py
```

---

# 💡 Key Takeaways

* Large Language Models are stateless.
* LangChain manages prompts and conversation flow.
* Prompt Templates provide structured communication with the model.
* RunnableWithMessageHistory is the modern approach for conversation memory.
* Streamlit Session State preserves UI state.
* LangSmith enables monitoring and debugging.
* Modular code is easier to maintain and extend.

---

# 🚀 Future Roadmap

This project will continue to evolve as I learn more about the LangChain ecosystem.

Planned enhancements include:

* Prompt Engineering
* Structured Output Parsing
* Multi-Chat Sessions
* Retrieval-Augmented Generation (RAG)
* PDF Chatbot
* Embeddings
* Vector Databases (FAISS / Chroma)
* Tool Calling
* AI Agents
* LangGraph
* Production Deployment

---

# 📖 Learning Notes

One of the biggest lessons from this project is that **LLMs do not have memory**. Every request is independent. It is the application's responsibility to reconstruct the conversation by storing previous messages and injecting them into each new prompt.

Another key lesson is the importance of software architecture. By separating the UI, model initialization, prompt design, conversation history, and chain composition into different modules, the application becomes easier to understand, maintain, and extend.

This project marks the beginning of my journey into building production-ready AI applications using LangChain.
