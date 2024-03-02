from fastapi import APIRouter, Depends
from models.UserModel import User
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal


AccountRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@AccountRouter.post("/login")
def login():
    
    return

@AccountRouter.post("/refreshToken")
def refreshToken():
    
    return