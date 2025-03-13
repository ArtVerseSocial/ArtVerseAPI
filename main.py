"""

"""
from fastapi import FastAPI
from config.ConfigManager import ConfigManager
from routes.AccountRouter import AccountRouter
from middlewares.AuthMiddleware import authenticateToken
from routes.PostRouter import PostRouter
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False}) # Initialization d'une api FastAPI#app.include_router(AccountRouter, prefix="/account") # Création d'un groupe de route avec comme prefix "user" donc -> "http://localhost:7676/user/..."

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Création d'un schéma d'authentification

app.include_router(AccountRouter, prefix="/auth") # Création d'un groupe de route avec comme prefix "auth" donc -> "http://localhost:7676/auth/*"
app.include_router(PostRouter, prefix="/post", dependencies=Depends(authenticateToken)) # Création d'un groupe de route avec comme prefix "post" donc -> "http://localhost:7676/post/*", avec une dépendance pour vérifier le token et le compte en même temps

# code pour pouvoir lancer l'api avec le server uvicorn
if __name__ == "__main__":
    import uvicorn # Importation du serveur uvicorn
    uvicorn.run(app, host=ConfigManager.APP()["IP"], port=ConfigManager.APP()["PORT"], headers=[("Server", "API")]) # Utilisation des variables de l'applications puis le lancement de l'API