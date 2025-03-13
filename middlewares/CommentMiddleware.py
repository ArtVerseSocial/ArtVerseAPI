from fastapi import Request, Depends
from sqlalchemy.orm import Session
from models.PostModel import Comment, CommentCreate
from config.ConfigDatabase import SessionLocal

def getAllCommentsOfPost(post_id: int, db: Session = Depends(SessionLocal)): # Fonction pour récupérer tous les commentaires d'un post
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return comments

def createComment(request: Request, comment: CommentCreate, db: Session): # Fonction pour créer un commentaire
    new_comment = Comment(
        content=comment.content,
        post_id=comment.post_id,
        user_uuid=request.session.auth['user']['uuid']
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment

def updateComment( request: Request, comment: CommentCreate, db: Session = Depends(SessionLocal)): # Fonction pour mettre à jour un commentaire
    commentDB = db.query(Comment).filter(Comment.id == comment.id).first()
    if commentDB is None:
        return None # Comment non trouvé
    
    commentDB.content = comment.content
    
    db.commit()
    db.refresh(comment)
    return comment

def deleteComment(request: Request, comment_id: int, db: Session = Depends(SessionLocal)): # Fonction pour supprimer un commentaire
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is None:
        return None # Comment non trouvé
    
    db.delete(comment)
    db.commit()
    return comment

__all__ = ['getAllCommentsOfPost', 'createComment', 'updateComment', 'deleteComment'] # Exporte toutes les fonctions de ce fichier