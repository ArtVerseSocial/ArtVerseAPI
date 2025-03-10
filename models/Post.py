"""

"""
from sqlalchemy import Column, Integer, String, DateTime, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from pydantic import BaseModel
import uuid, string, secrets
from pytz import timezone

# Création d'une classe de base pour les modèles SQLAlchemy
Base = declarative_base()

# Définition de la classe User, représentant une table dans la base de données
class Post(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'post'

    # Définition des colonnes de la table
    id = Column(UUID, primary_key=True, default=id, unique=True, nullable=False)  # Colonne UUID, clé primaire, générée automatiquement
    username = Column(String, nullable=False, default=)  # Colonne Name en String
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Colonne Created At, avec valeur par défaut définie à l'heure actuelle
    imgpost = Column(String, nullable=False)  # Colonne Image en String
    description = Column(String, nullable=False)  # Colonne Description en String
    likes = Column(Integer, nullable=False)  # Colonne Likes en Integer
    comments = Column(Integer, nullable=False)  # Colonne Comments en Integer
    
    @staticmethod
    def get_current_time(arg1, arg2, target):
        paris_tz = timezone('Europe/Paris')
        return datetime.now(paris_tz)  # Fonction pour générer une date avec le fuseau horaire de Paris
    
    # Fonction pour générer un token
    # @staticmethod
    # def generateToken(arg1, arg2, target):
    #     alphabet = string.ascii_letters + string.digits
    #     target.token = ''.join(secrets.choice(alphabet) for _ in range(128))

event.listen(Post, 'before_insert', Post.get_current_time) # Ajoute d'un event listener pour générer une date avant la création d'un nouveau post