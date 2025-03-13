from fastapi import Request, status, Response, HTTPException, Depends, Query
from models.PostModel import Post
from models.UserModel import User
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal

def putLike(self, request: Request, post_id = Query, db: Session = Depends(SessionLocal)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    
    user = db.query(User).filter(User.uuid == request.session.auth['user']['uuid']).first()
    
    if user in post.likes.all():
        Post.likes.remove(user)
    else:
        Post.likes.add(user)
    # Save the post
    post.save()
    # Return a response
    return Response(status=status.HTTP_200_OK)