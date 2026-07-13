"""
app.py

FastAPI backend for the LangChain Story Generator.

Responsibilities:
1. Expose REST APIs.
2. Validate requests using Pydantic.
3. Call the LangChain story generator.
4. Return structured JSON responses.
"""

from fastapi import FastAPI, HTTPException

from backend.chain import generate_story
from backend.models import StoryRequest, StoryResponse

# ------------------------------------------------------------------
# Create FastAPI application.
# ------------------------------------------------------------------

app = FastAPI(
    title="LangChain Story Generator API",
    description="Generate creative stories using LangChain and Google Gemini.",
    version="1.0.0",
)

# ------------------------------------------------------------------
# Health check endpoint.
# ------------------------------------------------------------------

@app.get("/")
def home():
    """
    Verify that the API is running.
    """

    return {
        "status": "running",
        "message": "LangChain Story Generator API"
    }

# ------------------------------------------------------------------
# Story generation endpoint.
# ------------------------------------------------------------------

@app.post(
    "/generate_story",
    response_model=StoryResponse
)
def create_story(request: StoryRequest):
    """
    Generate a story based on the user's topic.
    """

    try:

        story = generate_story(request.topic)

        return StoryResponse(
            story=story
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )