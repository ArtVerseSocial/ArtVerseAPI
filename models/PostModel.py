"""
Fait par Marin
Création du model pour toutes les tables différentes tel que User, Post, Comment, Likes, dans la base de donnée   
"""
from sqlalchemy import Column, Integer, String, DateTime, event, BOOLEAN, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from pydantic import BaseModel
from models.UserModel import User
from pytz import timezone

# Création d'une classe de base pour les modèles SQLAlchemy
Base = declarative_base()

@staticmethod
def get_current_time(arg1, arg2, target):
    paris_tz = timezone('Europe/Paris')
    return datetime.now(paris_tz)  # Fonction pour générer une date avec le fuseau horaire de Paris

# Définition de la classe Post, représentant une table dans la base de données
class Post(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'post'

    # Définition des colonnes de la table
    id = Column(Integer, primary_key=True, unique=True, nullable=False)  # Colonne UUID, clé primaire, générée automatiquement
    title = Column(String, nullable=False)  # Colonne Title en String
    user_uuid = Column(UUID, ForeignKey(User.uuid), nullable=False)  # Colonne user_id, clé étrangère référant à la table user
    img = Column(String, nullable=False)  # Colonne Image en String (doit être en base64)
    description = Column(String, nullable=False)  # Colonne Description en String
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Colonne Created At, avec valeur par défaut définie à l'heure actuelle
    user = relationship("user", back_populates="post")  # Relation avec la table user
    comments = relationship("comment", back_populates="post")  # Relation avec la table comment
    likes = relationship("like", back_populates="post")  # Relation avec la table like

class PostCreate(BaseModel): # Création d'une classe de modèle pour la création d'un post
    title: str
    user_uuid: UUID
    img: str
    description: str
    

class PostUpdate(BaseModel): # Création d'une classe de modèle pour la mise à jour d'un post
    id: int
    title: str = None
    user_uuid: UUID = None
    img: str = None
    description: str = None

    class Config:
        arbitrary_types_allowed = True # Permet d'accepter les types arbitraires (ici, UUID)

event.listen(Post, 'before_insert', get_current_time) # Ajoute d'un event listener pour générer une date avant la création d'un nouveau post

class Like(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'like'

    # Définition des colonnes de la table
    id = Column(Integer, primary_key=True, unique=True, nullable=False)  # Colonne ID, clé primaire, générée automatiquement
    user_id = Column(UUID, ForeignKey(User.uuid), nullable=False)  # Colonne user_id, clé étrangère référant à la table user
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=True)  # Colonne Likescom en Integer, clé étrangère référant à la table comment
    post_id = Column(Integer, ForeignKey("post.id"), nullable=True)  # Colonne Likespost en Integer, clé étrangère référant à la table post

    # Relations
    comment = relationship("comment", back_populates="like")
    post = relationship("post", back_populates="like")
    user = relationship("user", back_populates="like")

# Ajout des relations inverses
Post.likes = relationship("like", order_by=Like.id, back_populates="post")

class Comment(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'comment'

    # Définition des colonnes de la table
    id = Column(Integer, primary_key=True, unique=True, nullable=False)  # Colonne ID, clé primaire, générée automatiquement
    user_id = Column(UUID, ForeignKey(User.uuid), nullable=False)  # Colonne user_id, clé étrangère référant à la table user
    content = Column(String, nullable=False)  # Colonne contenu en String
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Colonne Created At, avec valeur par défaut définie à l'heure actuelle
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)  # Colonne post_id, clé étrangère référant à la table post
    # Relations
    user = relationship("user", back_populates="comment")
    post = relationship("post", back_populates="comment")

Post.comments = relationship('comment', order_by=Comment.id, back_populates='post')  # Ajoute la relation inverse dans la table Post

event.listen(Comment, 'before_insert', get_current_time) # Ajoute d'un event listener pour générer une date avant l'insertion d'un nouveau commentaire