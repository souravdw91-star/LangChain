"""
============================================================

app.py

This is the ONLY file responsible for the UI.

It should never contain business logic.

Business logic lives inside

1)llm.py
2)prompts.py
3)history.py
4)chain.py

Think of app.py as the receptionist.

It receives requests.

It shows responses.

It doesn't know HOW the AI works.

============================================================
"""

# ==========================================================
# Imports
# ==========================================================
from dotenv import load_dotenv

import streamlit as st
import os

from src.langsmith_config import configure_langsmith


# ==========================================================
# Load Environment Variables
#
# Loads values from .env
#
# We never hardcode API keys.
# ==========================================================

load_dotenv()
langsmith_config = configure_langsmith()

from src.chain import conversation_chain


# ==========================================================
# Configure Streamlit Page
# ==========================================================

st.set_page_config(

    page_title="LangChain Learning",

    page_icon="🤖",

    layout="wide"

)


st.title("🤖 LangChain + Gemini")

st.caption("Learning Modern LangChain")

if not langsmith_config["api_key_present"]:
    st.warning(
        "LangSmith tracing is disabled because no LangSmith API key was found. "
        "Add LANGCHAIN_API_KEY or LANGSMITH_API_KEY to your .env file to enable traces."
    )
elif not langsmith_config["tracing_enabled"]:
    st.warning(
        "LangSmith tracing is disabled because the API key could not be authenticated. "
        f"Details: {langsmith_config['validation_error']}"
    )


# ==========================================================
# Session State
#
# Streamlit reruns this script after every interaction.
#
# Session State keeps variables alive.
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================================
# Display Previous Conversation
#
# We redraw the chat from session state every rerun.
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================================
# User Input
# ==========================================================

user_question = st.chat_input(

    "Ask me anything..."

)


if user_question:

    # ------------------------------------------
    # Show User Message
    # ------------------------------------------

    st.session_state.messages.append(

        {

            "role": "user",

            "content": user_question

        }

    )

    with st.chat_message("user"):

        st.markdown(user_question)


    # ------------------------------------------
    # Invoke LangChain
    #
    # session_id identifies one conversation.
    #
    # Later this could become
    #
    # user email
    # UUID
    # database id
    #
    # etc.
    # ------------------------------------------

    response = conversation_chain.invoke(

        {

            "question": user_question

        },

        config={

            "configurable": {

                "session_id": "default"

            }

        }

    )


    # ------------------------------------------
    # Display AI Response
    # ------------------------------------------

    with st.chat_message("assistant"):

        st.markdown(response)


    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": response

        }

    )