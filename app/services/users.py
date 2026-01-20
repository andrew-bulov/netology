import logging
from dataclasses import dataclass

from app.db.users import fetch_users

logger = logging.getLogger(__name__)


@dataclass
class User:
    id: int
    name: str


def create_user(name: str) -> User:
    if not name:
        raise ValueError("Name is required")

    return User(id=1, name=name)


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
    logger.debug("Users: %s", users)
    logger.info("Fetched %d users", len(users))
    return users
