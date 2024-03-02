from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.SportModel import SportList
from config.ConfigDatabase import SessionLocal

AuthRouter = APIRouter() # Création d'un groupe de route avec comme prefix "sport" donc -> "http://localhost:7676/sport/..."

@AuthRouter.post("/login")
def login(db: Session = Depends(SessionLocal)):
    
    return

@AuthRouter.post("/refreshToken")
def refreshToken(db: Session = Depends(SessionLocal)):
    
    return