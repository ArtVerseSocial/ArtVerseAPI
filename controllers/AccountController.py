from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from models.UserModel import User, UserCreate
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError
import base64

def createUser(user, db: Session = Depends(SessionLocal)):
    db.add(user)
    db.commit()  # Confirmez la transaction
    db.expire(user)

    db.refresh(user)

    token_user = base64.standard_b64encode(f'{user.username}:{user.key_token}'.encode('utf-8'))

    raise HTTPException(status_code=status.HTTP_201_CREATED, detail={"status": 'User created', "token": token_user})

def registerController(user: UserCreate, db):
    new_user = User(username=user.username, email=user.email, password=user.password)
    
    # Validation des données
    if not new_user.username or not new_user.email or not new_user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')

    try: 
        validate_email(new_user.email)
    except EmailNotValidError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Invalid Email')

    if db.query(User).filter(User.email == new_user.email).first() or db.query(User).filter(User.username == new_user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Email or Username already exists')

    if len(new_user.password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Password too short')

    return createUser(new_user, db)

def loginController(response: Response):


    return

def refreshTokenController():
    return