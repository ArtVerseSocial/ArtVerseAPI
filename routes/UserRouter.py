from fastapi import APIRouter, Depends
from models.UserModel import User
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal

userRouter = APIRouter() # Création d'une classe de router pour créer un groupe de route

@userRouter.get("/list")
def get_users(db: Session = Depends(SessionLocal)):
    """
    Fonction qui permet de récupérer la liste des utilisateurs dans la table "user"

    :param db: Session de la base de donnée
    """
    users = db.query(User).all() # utilise la session pour faire une requête "query" qui récupére tout
    return users # Retourne la liste à la route