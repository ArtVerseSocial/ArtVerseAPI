from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.UserModel import User
from config.ConfigDatabase import SessionLocal

TestRouter = APIRouter()

@TestRouter.get("/user/list")
def test_get(db: Session = Depends(SessionLocal)):
    users = db.query(User).all()
    return users

@TestRouter.get("/user/create")
async def create_user(username: str, email: str, password: str, db: Session = Depends(SessionLocal)):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@TestRouter.get("/user/delete")
async def delete_user(username: str, db: Session = Depends(SessionLocal)):
    user = db.query(User).filter(User.username == username).first()
    db.delete(user)
    db.commit()
    return user