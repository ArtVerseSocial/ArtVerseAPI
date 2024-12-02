from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.UserModel import User
from config.ConfigDatabase import SessionLocal

TestRouter = APIRouter()

@TestRouter.get("/user")
def test_get(db: Session = Depends(SessionLocal)):
    users = db.query(User).all()