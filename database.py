
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent / "meetings.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS meetings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                transcript TEXT NOT NULL,
                analysis TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_meeting(title, transcript, analysis):
    with get_connection() as connection:
        cursor = connection.execute("""
            INSERT INTO meetings (title, transcript, analysis)
            VALUES (?, ?, ?)
        """, (title, transcript, analysis))

        return cursor.lastrowid


def get_all_meetings():
    with get_connection() as connection:
        return connection.execute("""
            SELECT id, title, created_at
            FROM meetings
            ORDER BY id DESC
        """).fetchall()


def get_meeting(meeting_id):
    with get_connection() as connection:
        return connection.execute("""
            SELECT id, title, transcript, analysis, created_at
            FROM meetings
            WHERE id = ?
        """, (meeting_id,)).fetchone()
