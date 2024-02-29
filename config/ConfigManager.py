class ConfigManager:
    DATABASE_URL: str = "postgres.oyrbbmyjxfwzntrrqjvi"
    DATABASE_PASSWORD: str = "nw_bz-q3?)ZX9N8"

    @classmethod
    def DATABASE(cls):
        return {
            "URL": cls.DATABASE_URL,
            "PASSWORD": cls.DATABASE_PASSWORD
        }

ConfigManager()