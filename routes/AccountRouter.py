"""
Info : Fait un group avec le prefix "/auth" pour les routes de l'authentification


"""
from fastapi import APIRouter, Depends, Header, Query, Response, status
from models.UserModel import UserCreate, UserLogin
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from controllers.AccountController import loginController, registerController, refreshController, deleteController
from fastapi import Query

AccountRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@AccountRouter.post("/register") # Création d'une nouvelle route register, pour créer son compte
async def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    return await registerController(user, db)

@AccountRouter.delete("/delete")
def delete(token: str = Header(None), db: Session = Depends(SessionLocal)):
    return deleteController(token, db)

@AccountRouter.post("/login")
def login(user: UserLogin, db: Session = Depends(SessionLocal)):
    return loginController(user, db)

@AccountRouter.post("/refresh")
def refresh(refreshToken: str = Header(None), db: Session = Depends(SessionLocal)):
    return refreshController(refreshToken)