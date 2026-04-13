import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME", "fixture")

    @staticmethod
    def validate():
        missing = []

        if not Config.DB_HOST:
            missing.append("DB_HOST")
        if not Config.DB_USER:
            missing.append("DB_USER")
        if not Config.DB_PASSWORD:
            missing.append("DB_PASSWORD")

        if missing:
            raise ValueError(
                f"Faltan las variables de entorno: {', '.join(missing)}. "
                "Revisa el archivo .env."
            )

    PORT = int(os.getenv("PORT", "5000"))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    DB_CONFIG = {
        "host": DB_HOST,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "database": DB_NAME
    }
