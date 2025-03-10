from fastapi import APIRouter, Depends, Header, Query, Response, status, HTTPException
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from models.UserModel import User, UserCreate, UserLogin
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.AuthMiddleware import generateAccessToken, generateRefreshToken
import base64,json
from passlib.context import CryptContext

def createUser(user: UserCreate, db: Session = Depends(SessionLocal)):
    temp_user = User(username=user.username, email=user.email, password=user.password)
    
    db.add(temp_user)
    db.commit()  # Confirme l'ajout d'un nouvel utilisateur dans la base de données

    user = db.query(User).filter(User.email == user.email).first()

    raise HTTPException(status_code=status.HTTP_201_CREATED, detail={"status": 'User created'})

async def registerController(user: UserCreate, db):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    
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

def loginController(user: UserLogin, db: Session = Depends(SessionLocal)):
    print(user)
    if not user.email or not user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad Request - Missing parameters')
    
    userDB = db.query(User).filter(User.email == user.email).first()
    if not userDB:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Email')
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    if not pwd_context.verify(user.password, userDB.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers='Unauthorized - Invalid Password')

    return {"AccessToken": generateAccessToken
    (userDB), "RefreshToken": generateRefreshToken(userDB)}

def refreshController(refreshToken: str = Header(None)):
    
    return