"""
===========================================================
File: llm.py

Purpose:
--------
This module is responsible for creating the Large Language Model (LLM).

Why create a separate file?

In production applications, the UI should never know
how the model is created.

Tomorrow we may switch from

Gemini
↓

OpenAI

or

Claude

or

Llama

without touching the Streamlit code.

This follows Separation of Concerns.
===========================================================
"""
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():
    """
    Creates and returns a Gemini chat model.

    Returns
    -------
    ChatGoogleGenerativeAI

    Temperature controls creativity.

    0.0 = deterministic

    1.0 = highly creative

    For learning and Q&A,
    0.3 is a good balance.
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    return llm