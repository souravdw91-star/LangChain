"""
frontend/app.py

Streamlit frontend for the LangChain Story Generator.

Responsibilities
----------------
1. Collect user input.
2. Call the FastAPI backend.
3. Display the generated story.
"""

import requests
import streamlit as st

# ------------------------------------------------------------------
# Backend API URL
# ------------------------------------------------------------------

API_URL = "http://127.0.0.1:8000/generate_story"

# ------------------------------------------------------------------
# Configure Streamlit page
# ------------------------------------------------------------------

st.set_page_config(
    page_title="LangChain Story Generator",
    page_icon="📖",
    layout="centered",
)

# ------------------------------------------------------------------
# Title
# ------------------------------------------------------------------

st.title("📖 LangChain Story Generator")

st.markdown(
    """
Generate creative stories using **LangChain**, **FastAPI**, and **Google Gemini**.
"""
)

# ------------------------------------------------------------------
# User Input
# ------------------------------------------------------------------

topic = st.text_input(
    "Enter a story topic"
)

# ------------------------------------------------------------------
# Generate Button
# ------------------------------------------------------------------

if st.button("Generate Story"):

    if not topic.strip():

        st.warning("Please enter a topic.")

        st.stop()

    with st.spinner("Generating story..."):

        try:

            response = requests.post(
                API_URL,
                json={
                    "topic": topic
                }
            )

            if response.status_code == 200:

                story = response.json()["story"]

                st.success("Story Generated!")

                st.write(story)

            else:

                st.error(
                    f"API Error : {response.status_code}"
                )

        except Exception as e:

            st.error(str(e))