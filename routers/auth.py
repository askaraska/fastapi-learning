from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from models.user import User as UserDB
from schemas.auth import UserCreate, UserResponse, UserLogin
from utils.security import hash_password, verify_password
from utils.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate,db: Session = Depends(get_db)):
    existing_username = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )

    existing_email = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(user.password)

    # Create the database user
    # This creates a SQLAlchemy object.
    db_user = UserDB(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(UserDB).filter(
        UserDB.username == form_data.username
        ).first()

    if not db_user:
        raise HTTPException(
            status_code= 401,
            detail= "Invalid username or password"
        )
    
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
    data={
        "sub": str(db_user.id)
    }
)

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }
