from fastapi import APIRouter, Depends
from models.UserModel import User
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal

AccountRouter = APIRouter() # Création d'une classe de router pour créer un groupe de route

@AccountRouter.get("/list")
def get_account(db: Session = Depends(SessionLocal)):
    """
    Fonction qui permet de récupérer la liste des utilisateurs dans la table "user"

    :param db: Session de la base de donnée
    """
    account = db.query(User).all() # utilise la session pour faire une requête "query" qui récupére tout
    return account # Retourne la liste à la route