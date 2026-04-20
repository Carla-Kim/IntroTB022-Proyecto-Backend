import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", "5000"))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "fixture")

APP_CONFIG = {
    "port": PORT,
    "debug": DEBUG
}

DB_CONFIG = {
    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASSWORD,
}

def validate_config():
    missing = []

    if not DB_HOST:
        missing.append("DB_HOST")
    if not DB_USER:
        missing.append("DB_USER")
    if not DB_PASSWORD:
        missing.append("DB_PASSWORD")

    if missing:
        raise RuntimeError(f"Faltan variables: {', '.join(missing)}")
