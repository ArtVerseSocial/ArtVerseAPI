from sqlalchemy import Column, Integer, String, DateTime, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from pydantic import BaseModel
import uuid, string, secrets

# Création d'une classe de base pour les modèles SQLAlchemy
Base = declarative_base()

def generateToken():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(128))

# Définition de la classe User, représentant une table dans la base de données
class User(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'user'

    # Définition des colonnes de la table
    id = Column(Integer, primary_key=True)  # Colonne ID, clé primaire
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Colonne UUID, clé primaire, générée automatiquement
    key_token = Column(String, unique=True, default=generateToken)  # Colonne Key Token en String, unique
    username = Column(String)  # Colonne Name en String
    email = Column(String)  # Colonne Email en String
    password = Column(String)  # Colonne Password en String
    created_at = Column(DateTime, default=datetime.utcnow)  # Colonne Created At, avec valeur par défaut définie à l'heure actuelle


class UserCreate(BaseModel):
    username: str
    email: str
    password: str