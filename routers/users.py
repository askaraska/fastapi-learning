from fastapi import APIRouter
from schemas.models import User
from typing import Optional


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

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