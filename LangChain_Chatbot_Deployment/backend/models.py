"""
models.py

This module contains all the request and response models
used by the FastAPI application.

FastAPI uses Pydantic models to:
1. Validate incoming requests.
2. Validate outgoing responses.
3. Automatically generate Swagger documentation.
"""

from pydantic import BaseModel


class StoryRequest(BaseModel):
    """
    Request model for story generation.

    Expected JSON from the frontend:

    {
        "topic": "The Last Dragon"
    }
    """

    topic: str


class StoryResponse(BaseModel):
    """
    Response model returned by the API.

    Example Response:

    {
        "story": "Once upon a time..."
    }
    """

    story: str