from fastapi import APIRouter, Depends, Header, Query, Response, status
from models.UserModel import UserCreate
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from controllers.AccountController import loginController, registerController, refreshTokenController
from fastapi import Query

AccountRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@AccountRouter.post("/register")
async def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    return await registerController(user, db)

@AccountRouter.post("/login")
def login(body: dict, db: Session = Depends(SessionLocal)):
    return loginController(body, db)

@AccountRouter.post("/refreshToken")
def refreshToken(token: str = Header(None)):
    return refreshTokenController(token)