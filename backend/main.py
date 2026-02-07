# backend/main.py
# FastAPI application entry point.
# Exposes the POST /chat endpoint for the frontend.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ChatRequest, ChatResponse
from database import init_db, save_message
from ai_logic import process_message

# Initialize FastAPI app
app = FastAPI(
    title="AI Personal Psychologist",
    description=(
        "A research prototype for a supportive, evidence-informed mental wellness assistant. "
        "This tool is NOT a substitute for professional mental health care or emergency services."
    ),
    version="0.1.0",
)

# Allow CORS for frontend (for local development and demo)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """
    Initialize resources on startup.
    Here we create the SQLite database and table if they do not exist.
    """
    init_db()


@app.get("/")
def home():
    """
    GET /
    Health check endpoint.
    """
    return {"status": "AI Personal Psychologist backend is running", "version": "0.1.0"}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    """
    POST /chat
    - Accepts a user message.
    - Runs it through the safety layer and supportive response generator.
    - Stores the interaction in the database.
    - Returns the AI reply and crisis flag.
    """
    user_message = payload.message.strip()
    reply, is_crisis = process_message(user_message)

    # Store in the database
    save_message(user_message=user_message, bot_reply=reply)

    return ChatResponse(reply=reply, is_crisis=is_crisis)
