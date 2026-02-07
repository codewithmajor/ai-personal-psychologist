# AI Personal Psychologist

A full-stack research prototype for an **AI Personal Psychologist** web application.
The goal is to offer supportive, evidence-informed mental wellness interactions focused on stress relief, emotional validation, and self-help.
This system **does not** provide diagnosis and **must not** be used as a replacement for therapy, medical care, or crisis services.

---

## Project Overview

This project is designed for academic use in an M.Tech context.
It demonstrates a simple but well-structured full-stack architecture using:

- Frontend: HTML, CSS, JavaScript (vanilla)
- Backend: Python **FastAPI**
- Database: **SQLite** (for storing interactions)

Key properties:

- Transparent rule-based "AI" behavior (no external LLM required)
- Explicit safety layer for crisis-related language
- Clear separation between frontend, backend, and data storage

---

## Features

- Chat-based interface with a clean UI.
- Empathetic, supportive AI responses that:
  - Validate feelings.
  - Maintain a hopeful and respectful tone.
  - Suggest small, practical coping strategies (breathing, hydration, light movement).
  - Avoid any medical or psychiatric diagnosis.
- Safety layer:
  - If user messages contain crisis-related keywords (e.g., "suicide", "kill myself", "self harm", "die"),
    the system returns a dedicated crisis response encouraging the user to contact emergency services or a helpline.
  - In crisis mode, the system does not produce a normal conversational reply.
- Data storage:
  - Each interaction (timestamp, user message, bot reply) is stored in a local SQLite database.
- Modular code layout for academic demonstration and future extension.

---

## Architecture

```text
ai-personal-psychologist/
  backend/
    main.py        # FastAPI app, /chat endpoint, wiring
    database.py    # SQLite connection and insert logic
    models.py      # Reserved for potential ORM models (kept simple here)
    schemas.py     # Pydantic request/response models
    ai_logic.py    # Safety checks and rule-based "AI" response generator
  frontend/
    index.html     # Chat UI layout and disclaimer
    styles.css     # Minimalistic, responsive styles
    app.js         # Frontend logic for calling /chat and rendering messages
  README.md
```

Request flow:

1. User types a message in the web interface.
2. Frontend sends a `POST /chat` request (JSON) to the FastAPI backend.
3. Backend checks for crisis-related content using keyword matching.
4. If crisis content is detected:
   - Backend returns a crisis response.
   - No normal AI chat response is generated.
5. If no crisis detected:
   - Backend generates a structured, supportive response.
6. Interaction (timestamp, user message, bot reply) is stored in SQLite.
7. Frontend displays the AI reply in the chat window.

---

## How to Run the Backend

### 1. Create and activate a virtual environment (recommended)

```bash
cd ai-personal-psychologist

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Start the FastAPI backend

From the `backend/` folder:

```bash
cd backend
uvicorn main:app --reload
```

By default, the API will be available at:

- `http://127.0.0.1:8000`

You can test the `/chat` endpoint using:

- `http://127.0.0.1:8000/docs` (interactive Swagger UI)

---

## How to Run the Frontend

For a simple static setup, you can open the `frontend/index.html` file directly in your browser.
However, for proper CORS behavior and to mimic a real deployment, you can serve it via a simple HTTP server.

From the `frontend/` folder:

```bash
cd frontend

# Option 1: Python simple server
python -m http.server 5500
```

Then open:

- `http://127.0.0.1:5500/index.html`

Ensure the `BACKEND_URL` in `frontend/app.js` matches where your FastAPI backend is running (default: `http://127.0.0.1:8000/chat`).

---

## Ethical Notice

- This project is **strictly** for educational and research purposes.
- The system:
  - Does **not** provide diagnosis, treatment, or medical advice.
  - Is **not** a licensed mental health professional.
  - Must **not** be used as a replacement for therapy, counseling, or emergency services.
- If a user is in immediate danger, they should contact:
  - Local emergency services, or
  - A trusted person, or
  - A licensed mental health professional, or
  - A crisis helpline, where available.

Any deployment or demonstration should explicitly communicate these limitations to participants.

---

## Future Work

- Replace or augment the rule-based engine with a real LLM (while preserving safety constraints).
- Extend crisis detection using NLP models instead of simple keywords.
- Add user accounts and privacy controls.
- Log interactions in an anonymized way for research (subject to ethics approval and data protection regulations).
