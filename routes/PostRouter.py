from fastapi import APIRouter, Depends, HTTPException, status, Request, Body
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from models.PostModel import Post, PostCreate, PostUpdate, PostLike
from middlewares.PostMiddleware import createPost, updatePost, deletePost, getPost
from middlewares.AuthMiddleware import authenticateToken
from middlewares.LikeMiddleware import switchLikeToPost
import base64

PostRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@PostRouter.get("/get") # Création d'une route GET pour récupérer tous les articles
def getArt(post_id: int = None, db: Session = Depends(SessionLocal)):
    posts = getPost(post_id, db) # Récupération des articles
    return posts # Retourne la liste des posts

@PostRouter.post("/create") # Création d'une route POST pour créer un nouvel article
async def postArt(request: Request,post: PostCreate, db: Session = Depends(SessionLocal)): # Définition de la fonction de la route
    if not post.title or not post.img or not post.description:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    try: # Vérification que l'image est bien en base64
        base64.b64decode(post.img, validate=True)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - img must be base64 encoded')
    
    new_post = createPost(request, post, db) # Création de l'article dans la base de données
    return new_post

@PostRouter.put("/update")
async def updateArt(request: Request, post: PostUpdate = Body(...), db: Session = Depends(SessionLocal)):
    # Vérification des paramètres
    if not post.id: # Vérification des paramètres
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    return await updatePost(request, post, db)

@PostRouter.delete("/delete")
async def deleteArt(request: Request, postId: int, db: Session = Depends(SessionLocal)):
    if not postId: # Vérification des paramètres
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    post = db.query(Post).filter(Post.id == postId).first()
    
    if not post: # Vérification que le post existe
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found - Post not found')
    
    return await deletePost(request, postId, db)

@PostRouter.post("/{post_id}/like")
def like_post(request: Request, post_id: int, db: Session = Depends(SessionLocal)):
    if not post_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found - Post not found')
    
    return switchLikeToPost(request, post_id, db)

@PostRouter.post("/{post_id}/comment")
def comment_post(post_id: int, comment: str, token: str = Depends(authenticateToken)):
    # Logique pour commenter un post
    pass