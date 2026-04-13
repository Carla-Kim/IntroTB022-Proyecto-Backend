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

    with open("database/init_db.sql", "r") as f:
        sql = f.read()

    cursor.execute(sql, multi=True)

    conn.commit()

    print("Base de datos inicializada correctamente.")

except mysql.connector.Error as err:
    print(f"Error al inicializar la base de datos: {err}")

except FileNotFoundError:
    print("No se encontró el archivo init_db.sql.")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
