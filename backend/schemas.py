# backend/schemas.py
# Defines Pydantic models for request and response bodies.

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Schema for incoming chat messages from the frontend.
    """
    message: str = Field(..., min_length=1, description="User's message to the AI assistant.")


class ChatResponse(BaseModel):
    """
    Schema for AI responses sent back to the frontend.
    """
    reply: str = Field(..., description="AI assistant's reply text.")
    is_crisis: bool = Field(False, description="True if message triggered crisis protocol.")
