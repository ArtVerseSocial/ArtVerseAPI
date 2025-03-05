from fastapi import APIRouter, Depends, Header, Query, Response, status, HTTPException
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from models.UserModel import User, UserCreate
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.AuthMiddleware import generateAccessToken, generateRefreshToken
import base64,json

def createUser(user: UserCreate, db: Session = Depends(SessionLocal)):
    temp_user = User(username=user.username, email=user.email, password=user.password)
    
    db.add(temp_user)
    db.commit()  # Confirme l'ajout d'un nouvel utilisateur dans la base de données

    user = db.query(User).filter(User.email == user.email).first()

    raise HTTPException(status_code=status.HTTP_201_CREATED, detail={"status": 'User created'})


async def registerController(user: UserCreate, db):
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

    return await createUser(new_user, db)

def deleteController(token: str = Header(None), db: Session = Depends(SessionLocal)):
    if not token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')

    user = db.query(User).filter(User.token == token).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Token')
    
    db.delete(user)
    db.commit()
    return {"status": "User deleted"}

def loginController(body: dict, db: Session = Depends(SessionLocal)):
    if not body["token"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    token = str(body["token"])
    temp_token = base64.standard_b64decode(str(token))
    temp_token_str = temp_token.decode('utf-8').split('/')
    key_token = temp_token_str[1]

    user = db.query(User).filter(User.key_token == key_token).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Token')
    
    AccessToken = generateAccessToken(user)
    RefreshToken = generateRefreshToken(user)
    
    return {"AccessToken": AccessToken, "RefreshToken": RefreshToken}

def refreshController(token: str = Header(None)):
    print("")
    return