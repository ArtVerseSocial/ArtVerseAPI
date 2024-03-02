from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.
from config.ConfigDatabase import SessionLocal

SportRouter = APIRouter() # Création d'un groupe de route avec comme prefix "sport" donc -> "http://localhost:7676/sport/..."


@SportRouter.get("/list")
def get_sports(db: Session = Depends(SessionLocal)):
    sports = db.query(Sport).all()
    return sports