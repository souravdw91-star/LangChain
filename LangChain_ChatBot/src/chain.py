"""
===========================================================
chain.py

Purpose
-------
Creates the complete LangChain pipeline.

Prompt

↓

LLM

↓

Output Parser

↓

RunnableWithMessageHistory

This file glues all the building blocks together.
===========================================================
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

from src.llm import get_llm
from src.prompts import get_prompt
from src.history import get_session_history

# Create all individual components

llm = get_llm()

prompt = get_prompt()

parser = StrOutputParser()

# LCEL (LangChain Expression Language)

chain = prompt | llm | parser

# Add conversation history support

conversation_chain = RunnableWithMessageHistory(

    runnable=chain,

    get_session_history=get_session_history,

    input_messages_key="question",

    history_messages_key="history",
)