from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.ConfigManager import ConfigManager
from models.UserModel import User as UserModel
from models.PostModel import Post as PostModel

Config = ConfigManager.DATABASE() # Récupération des variables de la base de donnée

# Class pour pouvoir regrouper toute la configuration de la bdd (à ne pas toucher)
class ConfigDatabase:
    def __init__(self, url):
        try:
            self.engine = create_engine(url, echo=True) # Connexion à la base de donnée
            print("Success")
            UserModel.metadata.create_all(bind=self.engine) # Si table non créé, alors la créer
            PostModel.metadata.create_all(bind=self.engine) # Si table non créé, alors la créer
            self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine) # Création d'une session pour pouvoir manipuler la base de donnée
        except Exception as e:
            print(e)

    def get_session(self):
        return self.Session() # Mettre la session en public

# Utilisation de la classe ConfigDatabase pour créer la base de données et la session
config_db = ConfigDatabase(f'{Config["PROTOCOL"]}://{Config["USER"]}:{Config["PASSWORD"]}@{Config["HOST"]}:{Config["PORT"]}/{Config["NAME"]}')

SessionLocal = config_db.get_session # Initialization des variables externes