# app/services/users.py
import logging
from app.db.users import fetch_users

logger = logging.getLogger(__name__)


def get_users() -> list[dict]:
    logger.debug("Fetching users from database")

    rows = fetch_users()

    users = [
        {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "is_active": bool(row[3]),
            "created_at": row[4],
        }
        for row in rows
    ]

    logger.info("Fetched %d users", len(users))
    return users
