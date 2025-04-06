import sqlite3
import os

DB_PATH = "database/hire_smart.db"

def init_db():
    """Initializes the SQLite database and creates required tables."""
    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop and recreate the table every time for fresh state
    cursor.execute("DROP TABLE IF EXISTS candidates")

    cursor.execute("""
        CREATE TABLE candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            cv_path TEXT,
            score REAL,
            status TEXT,
            matched_jd TEXT,
            interview_date TEXT,
            interview_time TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized and table ready (reset).")

def store_results(shortlisted: list):
    """
    Stores shortlisted candidates in the database.
    """
    if not shortlisted:
        print("⚠️ No candidates to store.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for candidate in shortlisted:
        cursor.execute("""
            INSERT INTO candidates (
                name, email, phone, cv_path, score, status,
                matched_jd, interview_date, interview_time
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            candidate.get("name"),
            candidate.get("email"),
            candidate.get("phone"),
            candidate.get("cv_path"),
            candidate.get("score"),
            candidate.get("status", "shortlisted"),
            candidate.get("job_title"),
            candidate.get("interview_date"),
            candidate.get("interview_time")
        ))

    conn.commit()
    conn.close()
    print(f"📦 Stored {len(shortlisted)} candidates in the database.")
