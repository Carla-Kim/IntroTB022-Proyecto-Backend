import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conn.cursor()

with open("database/init_db.sql", "r") as f:
    sql = f.read()

cursor.execute(sql, multi=True)

conn.commit()
cursor.close()
conn.close()