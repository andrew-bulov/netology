# app/api/users.py
from fastapi import APIRouter
from app.services.users import get_users

router = APIRouter()


@router.get("/users")
def list_users():
    return get_users()
