import mysql.connector
from app.config import Config

def get_connection():
    try:
        return mysql.connector.connect(**Config.DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        raise
