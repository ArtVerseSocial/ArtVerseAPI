# Fichier de configuration de l'api

class ConfigManager:
    # Variable de configuration de l'application
    APP_IP: str = "127.0.0.1" # Variable: APP_IP
    APP_PORT: int = 7676

    DATABASE_HOST: str = "aws-0-eu-central-1.pooler.supabase.com" # Variable: DATABASE_HOST qui contient le nom de l'host de connexion à la base de donnée
    DATABASE_PORT: int = 5432 # Variable DATABASE_PORT qui contient le port de l'host de connexion à la base de donnée
    DATABASE_USER: str = "postgres.oyrbbmyjxfwzntrrqjvi" # Variable: DATABASE_USER qui contient l'identifiant de l'utilisateur de connexion à la base de donnée
    DATABASE_PASSWORD: str = "nw_bz-q3?)ZX9N8" # Variable: DATABASE_PASSWORD qui contient le mot de passe de l'utilisateur de connexion à la base de donnée

    @classmethod
    def APP(cls):
        keys = ["IP", "PORT"]
        return {key: getattr(cls, f"APP_{key}") for key in keys} # Boucle pour récupérer les variables contenant le prefix "APP"

    @classmethod
    def DATABASE(cls): # Définition des variables au groupe DATABASE -> ConfigManager.DATABASE()["...."]
        keys = ["HOST", "PORT", "USER", "PASSWORD"]
        return {key: getattr(cls, f"DATABASE_{key}") for key in keys} # Boucle pour récupérer les variables contenant le prefix "DATABASE"

ConfigManager()