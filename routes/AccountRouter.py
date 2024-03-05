from fastapi import APIRouter, Depends, Response, status
from models.UserModel import UserCreate
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from controllers.AccountController import loginController, registerController, refreshTokenController

AccountRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@AccountRouter.post("/register")
def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    return registerController(user, db)

@AccountRouter.post("/login")
def login():
    return loginController()

@AccountRouter.post("/refreshToken")
def refreshToken():
    return refreshTokenController()

@AccountRouter.get("/test")
def test():
    return "test"