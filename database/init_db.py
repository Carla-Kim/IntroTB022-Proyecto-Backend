import mysql.connector
from app.config import *

validate_config()

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SHOW DATABASES LIKE 'fixture'")
    initialized = cursor.fetchone()

    if initialized:
        print("La base de datos ya existe. Saltando inicialización.")
    else:
        with open("database/init_db.sql", "r", encoding="utf-8") as f:
            sql_init = f.read()

        for line in sql_init.split(';'):
            if line.strip():
                cursor.execute(line)

        conn.commit()
        print("Base de datos 'fixture' e información inicial cargada.")

except mysql.connector.Error as err:
    print(f"Error de MySQL: {err}")

except FileNotFoundError:
    print("Archivo database/init_db.sql no encontrado.")

finally:
    cursor.close()
    conn.close()
