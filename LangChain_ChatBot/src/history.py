"""
===========================================================
history.py

Purpose
-------
Stores chat history.

Think of this as the notebook where every conversation
is written down.

Gemini never remembers anything.

LangChain stores messages here and sends them back
to Gemini whenever a new question is asked.

Today we will use in-memory storage.

Later we can replace this with:

• Redis
• PostgreSQL
• MongoDB
• DynamoDB

without changing our chain.
===========================================================
"""

from langchain_core.chat_history import InMemoryChatMessageHistory

# Dictionary that stores all conversations.
#
# Key   -> Session ID
#
# Value -> Chat History

store = {}


def get_session_history(session_id: str):

    """
    Returns chat history for one conversation.

    If this is the user's first message,
    create an empty history.

    Otherwise return the existing history.
    """

    if session_id not in store:

        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]