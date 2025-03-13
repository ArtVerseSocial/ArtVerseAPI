from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from models.PostModel import Post, PostCreate, PostUpdate
from middlewares.PostMiddleware import createPost, updatePost
from middlewares.AuthMiddleware import authenticateToken
import base64

PostRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@PostRouter.get("/get") # Création d'une route GET pour récupérer tous les articles
async def getArt(db: Session = Depends(SessionLocal)):
    posts = db.query(Post).order_by(Post.created_at).all() # Récupération de tous les articles dans la base de données
    return posts # Retourne la liste des posts

@PostRouter.post("/create") # Création d'une route POST pour créer un nouvel article
async def postArt(post: PostCreate, db: Session = Depends(SessionLocal)): # Définition de la fonction de la route
    if not post.title or not post.img or not post.description:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    try: # Vérification que l'image est bien en base64
        base64.b64decode(post.img)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - img must be base64 encoded')
    
    new_post = createPost(post, db) # Création de l'article dans la base de données
    return new_post

@PostRouter.put("/update")
async def updateArt(post: PostUpdate, db: Session = Depends(SessionLocal)):
    # Vérification des paramètres
    if not post.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    updatePost(post, db)
    
    return {"status": "Post updated"}

@PostRouter.delete("/delete")
async def deleteArt(postId: int, db: Session = Depends(SessionLocal)):
    if not postId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    post = db.query(Post).filter(Post.id == postId).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    
    db.delete(post)
    db.commit()
    
    return {"status": "Post deleted"}

@PostRouter.post("/{post_id}/like")
def like_post(post_id: int, token: str = Depends(authenticateToken)):
    # Logique pour liker un post
    pass

@PostRouter.post("/{post_id}/comment")
def comment_post(post_id: int, comment: str, token: str = Depends(authenticateToken)):
    # Logique pour commenter un post
    pass