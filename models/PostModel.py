"""
Fait par Marin
Création du model pour toutes les tables différentes tel que User, Post, Comment, Likes, dans la base de donnée   
"""
from sqlalchemy import Column, Integer, String, DateTime, event, BOOLEAN, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime
from pydantic import BaseModel
import uuid, string, secrets
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
    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False)  # Colonne UUID, clé primaire, générée automatiquement
    username = mapped_column(String, nullable=False)  # Colonne Name en String
    img_post = mapped_column(String, nullable=False)  # Colonne Image en String
    description = mapped_column(String, nullable=False)  # Colonne Description en String
    created_at = mapped_column(DateTime, default=datetime.utcnow, nullable=False)  # Colonne Created At, avec valeur par défaut définie à l'heure actuelle

event.listen(Post, 'before_insert', get_current_time) # Ajoute d'un event listener pour générer une date avant la création d'un nouveau post

class Like(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'like'

    # Définition des colonnes de la table
    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False)  # Colonne ID, clé primaire, générée automatiquement
    username = mapped_column(String, nullable=False)  # Colonne Name en String
    # comment_id = mapped_column(Integer, ForeignKey("comment.id"), nullable=False)  # Colonne Likescom en Integer 
    # post_id = mapped_column(Integer, ForeignKey("post.id"), nullable=False)  # Colonne Likespost en Integer

class Comment(Base):
    # Nom de la table dans la base de données
    __tablename__ = 'comment'

    # Définition des colonnes de la table
    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False)  # Colonne ID, clé primaire, générée automatiquement
    username = mapped_column(String, nullable=False)  # Colonne Name en String
    content = mapped_column(String, nullable=False)  # Colonne contenu en String
    created_at = mapped_column(DateTime, default=datetime.utcnow, nullable=False)  # Colonne Created At, avec valeur par défaut définie à l'heure actuelle
    # post_id = mapped_column(Integer, ForeignKey('post.id'), nullable=False)  # Colonne post_id, clé étrangère référant à la table post

# Post.comments = relationship('Comment', order_by=Comment.id, back_populates='post')  # Ajoute la relation inverse dans la table Post

event.listen(Comment, 'before_insert', get_current_time) # Ajoute d'un event listener pour générer une date avant l'insertion d'un nouveau commentaire