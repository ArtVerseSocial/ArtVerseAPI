from fastapi import FastAPI
from routes.AccountRouter import AccountRouter
from routes.SportRouter import SportRouter
from routes.AuthRouter import AuthRouter
from config.ConfigManager import ConfigManager

app = FastAPI() # Initialization d'une api FastAPI

app.include_router(AccountRouter, prefix="/user") # Création d'un groupe de route avec comme prefix "user" donc -> "http://localhost:7676/user/..."
app.include_router(SportRouter, prefix="/sport") # Création d'un groupe de route avec comme prefix "sport" donc -> "http://localhost:7676/sport/..."
app.include_router(AuthRouter, prefix="/login")

# code pour pouvoir lancer l'api avec py et non uvicorn
if __name__ == "__main__":
    import uvicorn # Importation du serveur uvicorn
    uvicorn.run(app, host=ConfigManager.APP()["IP"], port=ConfigManager.APP()["PORT"], headers=[("Server", "SportInsightAPI")]) # Utilisation des variables de l'applications puis le lancement de l'API