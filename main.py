from fastapi import FastAPI
from routes.UserRouter import userRouter
from config.ConfigManager import ConfigManager

app = FastAPI() # Initialization d'une api FastAPI

app.include_router(userRouter, prefix="/user") # Création d'un groupe de route avec comme prefix "user" donc -> "http://localhost:7676/user/..."
app.include_router()

# code pour pouvoir lancer l'api avec py et non uvicorn
if __name__ == "__main__":
    import uvicorn # Importation du serveur uvicorn
    uvicorn.run(app, host=ConfigManager.APP()["IP"], port=ConfigManager.APP()["PORT"], headers=[("Server", "SportInsightAPI")]) # Utilisation des variables de l'applications puis le lancement de l'API