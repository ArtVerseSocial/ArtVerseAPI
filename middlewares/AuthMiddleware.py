import jwt
from config.ConfigManager import ConfigManager
from models.UserModel import User
from datetime import datetime, timedelta
from fastapi import Response, status, Request, HTTPException

def tokenPayload(user: User):
    return {
        "uuid": str(user.uuid),
        "username": user.username,
        "email": user.email,
    }

expiredAccessToken = timedelta(hours=1)
expiredRefreshToken = timedelta(days=7)

def generateAccessToken(user):
    return jwt.encode(tokenPayload(user), ConfigManager.AUTH()["ACCESS_TOKEN"], algorithm='HS256')

def generateRefreshToken(user):
    return jwt.encode(tokenPayload(user), ConfigManager.AUTH()["REFRESH_TOKEN"], algorithm='HS256')

def formatJWT(token):
    parts = token.split('.')

    if len(parts) == 3:
        return True


def authenticateToken(authorization, response: Response, request: Request):
    token_prefix, token = authorization.split()

    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Bearer token')

    try:
        if not formatJWT(token):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Format Bearer token')

        user = jwt.decode(token, ConfigManager.API_KEY.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
        request.session.auth = request.session.get('auth', {})
        request.session.auth['user'] = user

        if request.session.auth['user']['username'] == 'root':
            request.session.auth['isRoot'] = True
        next()
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Bearer token')
    except Exception as e:
        print('Erreur lors de la vérification du token :', e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Bearer token')

async def refreshToken(token):
    if not formatJWT(token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Format Bearer token')

    try:
        user = jwt.decode(token, ConfigManager.API_KEY.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
        del user['iat']
        del user['exp']
        refreshedToken = await generateAccessToken(user)
        return refreshedToken
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized - Invalid Bearer token')

# Export des fonctions
__all__ = ['authenticateToken', 'generateAccessToken', 'generateRefreshToken', 'refreshToken']