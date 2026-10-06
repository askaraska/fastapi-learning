from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from models.user import User as UserDB
from utils.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(
    # """For endpoints that depend on this security scheme,
    #   look for a Bearer token in the Authorization header."""
    tokenUrl="/auth/login"
)

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
        payload = verify_access_token(token)

        if payload is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        try:
            user_id = int(user_id)

        except (TypeError, ValueError):
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )     

        db_user = db.query(UserDB).filter(
            UserDB.id == user_id
        ).first()

        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return db_user
