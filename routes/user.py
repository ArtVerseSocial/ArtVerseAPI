from fastapi import FastAPI, APIRouter, Depends
from models import User
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from fastapi.responses import JSONResponse

userRouter = APIRouter()

@userRouter.get("/list")
def get_users(db: Session = Depends(SessionLocal)):
    users = db.query(User).all()
    users_list = [{"id": user.id, "name": user.name} for user in users]
    return JSONResponse(content=users_list)