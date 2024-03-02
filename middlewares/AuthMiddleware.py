import jwt
from config.ConfigManager import ConfigManager
from datetime import datetime, timedelta

def tokenPayload(user):
    return {
        'id': user['id'],
        'username': user['username'],
        'token': user['token'],
        'createdAt': user['createdAt'],
        'updatedAt': user['updatedAt']
    }

expiredAccessToken = timedelta(hours=1)
expiredRefreshToken = timedelta(days=7)

def generateAccessToken(user):
    return jwt.encode(tokenPayload(user), ConfigManager.AUTH()["ACCESS_TOKEN"], algorithm='HS256', expires_in=expiredAccessToken)

def generateRefreshToken(user):
    return jwt.encode(tokenPayload(user), ConfigManager.AUTH()["REFRESH_TOKEN"], algorithm='HS256', expires_in=expiredRefreshToken)

def formatJWT(token):
    parts = token.split('.')

    if len(parts) == 3:
        return True


def authenticateToken(authorization):
    token_prefix, token = authorization.split()

    if not token:
        return res.status(499).json({ 'error': 'Unauthorized - Missing or invalid Bearer token' })

    try:
        if not formatJWT(token):
            return res.status(401).json({ 'error': 'Unauthorized - Invalid Format Bearer token' })

        user = jwt.decode(token, ConfigManager.API_KEY.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
        req.auth = req.get('auth', {})
        req.auth['user'] = user

        if req.auth['user']['username'] == 'root':
            req.auth['isRoot'] = True
        next()
    except jwt.ExpiredSignatureError:
        return res.status(498).json({ 'error': 'Unauthorized - Token Expired' })
    except Exception as e:
        print('Erreur lors de la vérification du token :', e)
        return res.status(401).json({ 'error': 'Unauthorized - Invalid Bearer token' })

async def refreshToken(res, token):
    if not formatJWT(token):
        raise Exception({ 'error': 'Unauthorized - Invalid Format Bearer token' })

    try:
        user = jwt.decode(token, ConfigManager.API_KEY.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
        del user['iat']
        del user['exp']
        refreshedToken = await generateAccessToken(user)
        return refreshedToken
    except jwt.ExpiredSignatureError:
        raise Exception({ 'error': 'Unauthorized - Invalid Bearer RefreshToken' })

# Export des fonctions
__all__ = ['authenticateToken', 'generateAccessToken', 'generateRefreshToken', 'refreshToken']