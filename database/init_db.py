import mysql.connector
from app.config import DB_CONFIG

conn = mysql.connector.connect(
    host=DB_CONFIG["host"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"]
)

cursor = conn.cursor()

with open("database/init_db.sql", "r") as f:
    sql = f.read()

cursor.execute(sql, multi=True)

conn.commit()
cursor.close()
conn.close()