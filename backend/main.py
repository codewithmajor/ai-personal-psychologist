from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Personal Psychologist API")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Backend is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    # Safety check
    if "suicide" in user_message or "kill myself" in user_message:
        return {
            "reply": "I’m really sorry you’re feeling this way. "
                     "If you are in danger, please contact emergency services or a suicide helpline immediately."
        }

    # Temporary AI response
    return {
        "reply": "Thank you for sharing. Would you like to try a short breathing exercise?"
    }
