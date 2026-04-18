import mysql.connector
from app.config import Config

Config.validate()

conn = None
cursor = None

try:
    conn = mysql.connector.connect(
        host=Config.DB_CONFIG["host"],
        user=Config.DB_CONFIG["user"],
        password=Config.DB_CONFIG["password"]
    )

    cursor = conn.cursor()

    with open("database/init_db.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    for result in sql.split(';'):
        if result.strip():
            cursor.execute(result)

    conn.commit()
    print("Base de datos 'fixture' e información inicial cargada.")

except mysql.connector.Error as err:
    print(f"Error de MySQL: {err}")
except FileNotFoundError:
    print("Archivo database/init_db.sql no encontrado.")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()