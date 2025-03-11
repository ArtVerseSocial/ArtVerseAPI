"""

"""
from fastapi import FastAPI
from config.ConfigManager import ConfigManager
from routes.AccountRouter import AccountRouter
from routes.PostRouter import PostRouter

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False}) # Initialization d'une api FastAPI#app.include_router(AccountRouter, prefix="/account") # Création d'un groupe de route avec comme prefix "user" donc -> "http://localhost:7676/user/..."

app.include_router(AccountRouter, prefix="/auth") # Création d'un groupe de route avec comme prefix "auth" donc -> "http://localhost:7676/auth/..."
app.include_router(PostRouter, prefix="/post") # Création d'un groupe de route avec comme prefix "post" donc -> "http://localhost:7676/post/..."

# code pour pouvoir lancer l'api avec le server uvicorn
if __name__ == "__main__":
    import uvicorn # Importation du serveur uvicorn
    uvicorn.run(app, host=ConfigManager.APP()["IP"], port=ConfigManager.APP()["PORT"], headers=[("Server", "API")]) # Utilisation des variables de l'applications puis le lancement de l'API