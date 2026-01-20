import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            is_active BOOLEAN NOT NULL DEFAULT 1,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()

    print(f"Database created at {DB_PATH}")
def seed_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executemany(
        """
        INSERT INTO users (name, email)
        VALUES (?, ?)
        """,
        [
            ("Ivan Ivanov", "ivan@test.ru"),
            ("Anna Petrova", "anna@test.ru"),
            ("Petr Sidorov", "petr@test.ru"),
        ]
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    seed_users()