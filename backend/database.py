# backend/database.py
# Handles SQLite database connection and table creation.

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from datetime import datetime

# Database file path (relative to backend folder)
DB_PATH = Path(__file__).parent / "conversations.db"


def init_db():
    """Create the conversations table if it does not exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                user_message TEXT NOT NULL,
                bot_reply TEXT NOT NULL
            );
            """
        )
        conn.commit()


@contextmanager
def get_db():
    """
    Context manager to get a database connection.
    Ensures the connection is closed properly after use.
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


def save_message(user_message: str, bot_reply: str):
    """
    Save a single interaction (timestamp, user message, bot reply) to the database.
    """
    with get_db() as conn:
        cursor = conn.cursor()
        timestamp = datetime.utcnow().isoformat()
        cursor.execute(
            """
            INSERT INTO conversations (timestamp, user_message, bot_reply)
            VALUES (?, ?, ?);
            """,
            (timestamp, user_message, bot_reply),
        )
        conn.commit()
