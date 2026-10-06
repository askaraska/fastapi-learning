from fastapi import APIRouter, Depends
from schemas.models import User
from typing import Optional

from utils.auth import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/profile")
def get_profile(
    current_user = Depends(get_current_user)
):
    return {
        "message": "You are authenticated",
        "user_id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@router.get("/{user_id}")
def get_user(user_id: int):
    return{
        "user_id": user_id
    }

@router.post("")
def create_user(user: User): 
    # FastAPI, take the incoming JSON body and convert/validate it using the User model
    return{
        "message": "User created successfully",
        "user": user
    }


@router.get("/{user_id}/orders")
def get_user_orders(
    user_id: int,
    status: str,
    message: Optional[str] = None
):
    return {
        "user_id": user_id,
        "status": status,
        "message": message
    }

