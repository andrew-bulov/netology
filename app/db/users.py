from app.db.sqlite import get_connection

DB_PATH = "db/users.db"


def fetch_users() -> list[tuple]:
    conn = get_connection(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, is_active, created_at
        FROM users
        ORDER BY id
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
