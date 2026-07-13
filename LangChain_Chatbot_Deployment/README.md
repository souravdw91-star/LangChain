# LangChain Chatbot Deployment

## Overview

This project demonstrates how to deploy a LangChain-powered application using **FastAPI** as the backend and **Streamlit** as the frontend.

The application exposes a REST API that generates a story (maximum 500 words) based on a topic entered by the user. The frontend communicates with the backend through HTTP requests while the backend uses LangChain and Google Gemini to generate the response.

This project was built as part of a structured LangChain learning roadmap.

---

# Project Architecture

```
User
   │
   ▼
Streamlit Frontend
   │
HTTP POST Request
   ▼
FastAPI Backend
   │
Pydantic Validation
   ▼
LangChain Chain
   │
ChatPromptTemplate
   │
Google Gemini
   ▼
Generated Story
   │
JSON Response
   ▼
Streamlit UI
```

---

# Project Structure

```
LangChain/
│
├── .env
├── requirements.txt
│
└── LangChain_Chatbot_Deployment/
    │
    ├── backend/
    │   ├── __init__.py
    │   ├── app.py
    │   ├── chain.py
    │   └── models.py
    │
    └── frontend/
        ├── __init__.py
        └── app.py
```

---

# Features

* FastAPI REST API
* Streamlit user interface
* LangChain prompt pipeline
* Google Gemini integration
* ChatPromptTemplate
* LCEL (`prompt | llm`)
* Pydantic request validation
* Automatic Swagger documentation
* LangSmith tracing support
* Modular project structure

---

# Technologies Used

* Python
* LangChain
* Google Gemini
* FastAPI
* Streamlit
* Pydantic
* Requests
* Python Dotenv
* LangSmith

---

# API Endpoint

## Generate Story

**POST**

```
/generate_story
```

### Request

```json
{
    "topic": "The Last Dragon"
}
```

### Response

```json
{
    "story": "Once upon a time..."
}
```

---

# Running the Project

## 1. Activate the virtual environment

```
venv\Scripts\activate
```

## 2. Install dependencies

```
pip install -r requirements.txt
```

## 3. Start the backend

From the `LangChain_Chatbot_Deployment` directory:

```
uvicorn backend.app:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## 4. Start the frontend

Open a second terminal and run:

```
streamlit run frontend/app.py
```

---

# Workflow

1. User enters a topic in the Streamlit application.
2. Streamlit sends a POST request to the FastAPI backend.
3. FastAPI validates the request using Pydantic.
4. FastAPI calls the LangChain pipeline.
5. LangChain formats the prompt using `ChatPromptTemplate`.
6. Google Gemini generates the story.
7. FastAPI returns the response as JSON.
8. Streamlit displays the generated story.

---

# Learning Objectives

This project demonstrates:

* Building REST APIs with FastAPI
* Creating request and response models using Pydantic
* Using ChatPromptTemplate
* Prompt Engineering
* LangChain Expression Language (LCEL)
* Google Gemini integration
* Calling APIs from Streamlit
* Separating frontend and backend
* Environment variable management
* LangSmith observability

---

# Future Improvements

* Chat-style interface using `st.chat_input`
* Conversation memory
* Streaming responses
* Authentication
* Multiple prompt templates
* Docker support
* Cloud deployment
* Logging
* Unit tests
* LangServe integration

---

# Author

Created as part of a personal LangChain learning journey focused on building production-style LLM applications using FastAPI and Streamlit.
