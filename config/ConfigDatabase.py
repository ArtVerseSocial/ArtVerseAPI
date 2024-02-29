from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.ConfigManager import ConfigManager
from models import Base, User


class ConfigDatabase:
    def __init__(self, url):
        try:
            self.engine = create_engine(url, echo=True)
            print("Success")

            Base.metadata.create_all(bind=self.engine)
            self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        except Exception as e:
            print(e)

    def get_session(self):
        return self.Session()


# Utilisation de la classe ConfigDatabase pour créer la base de données et la session
config_db = ConfigDatabase(
    f'postgresql://{ConfigManager.DATABASE()["URL"]}:{ConfigManager.DATABASE()["PASSWORD"]}@aws-0-eu-central-1.pooler.supabase.com:5432/postgres')

SessionLocal = config_db.get_session
