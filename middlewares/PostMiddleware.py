from models.PostModel import Post, PostCreate
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from fastapi import Depends, HTTPException, status, Request

def getAllPost(db: Session = Depends(SessionLocal)):
    posts = db.query(Post).order_by(Post.created_at).all() # Récupération de tous les articles dans la base de données
    return posts # Retourne la liste des posts

def createPost(request: Request,post: PostCreate, db: Session = Depends(SessionLocal)):
    new_post = Post( # Création d'un nouvel objet Post avec les paramètres reçus
        title=post.title,
        img=post.img,
        description=post.description, 
        user_uuid=request.session.auth['user']['uuid']
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

def updatePost(request: Request, post: PostCreate, db: Session = Depends(SessionLocal)):
    postDB = db.query(Post).filter(Post.id == post.id).first()
    if request.session.auth['user']['uuid'] != postDB.user_uuid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - You are not the author of this post')
    
    if not postDB:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    
    for key, value in post.__dict__.items():
        if key != "id" and value is not None:
            setattr(postDB, key, value)
    
    db.commit()
    db.refresh(postDB)
    
    return postDB