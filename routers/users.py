from fastapi import Depends, APIRouter
from schemas import UsersCreate
from hashing import Hasher
from sqlalchemy.orm import Session
from database import get_db
from models import Base, User
from schemas import ShowUser


router = APIRouter()

@router.get("/users",tags=["user"])
def get_user():
    return {"message": "Hello User"}

@router.post("/users",tags=["user"],response_model=ShowUser)
def create_user(user: UsersCreate,db:Session=Depends(get_db)):
    user = User(email=user.email,password=Hasher.get_hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user