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
from pathlib import Path


def _find_env_file():
    """Locate the workspace root .env file by walking up from this module."""
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        env_path = parent / ".env"
        if env_path.exists():
            return env_path
    return current.parents[1] / ".env"


load_dotenv(dotenv_path=_find_env_file())

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("Google_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set. Add it to your .env file before running the app.")


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