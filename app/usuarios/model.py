from app.db import get_connection

def check_by_email(cursor, email):
    cursor.execute("SELECT 1 FROM usuarios WHERE email = %s", (email,))
    return cursor.fetchone() is not None

def check_by_id(cursor, id):
    cursor.execute("SELECT 1 FROM usuarios WHERE id_usuario = %s", (id,))
    return cursor.fetchone() is not None

def fetch_usuarios(cursor, limit, offset):
    sql_count = "SELECT COUNT(*) as count FROM usuarios"
    sql_elems = "SELECT id_usuario, nombre FROM usuarios LIMIT %s OFFSET %s"

    cursor.execute(sql_count)
    count = cursor.fetchone()["count"]

    cursor.execute(sql_elems, (limit, offset))
    rows = cursor.fetchall()

    return {
        "rows": rows,
        "count": count
    }

def insert_usuario(cursor, nombre, email):
    sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    cursor.execute(sql, (nombre, email))

    return cursor.lastrowid

def fetch_usuario(cursor, id):
    sql = "SELECT id_usuario, nombre, email FROM usuarios WHERE id_usuario = %s"
    cursor.execute(sql, (id,))

    return cursor.fetchone()

def actualizar_usuario_db(id_usuario, nombre, email):
    conexion = get_connection()
    cursor = conexion.cursor()
    try:
        query = "UPDATE usuarios SET nombre = %s, email = %s WHERE id_usuario = %s"
        cursor.execute(query, (nombre, email, id_usuario))
        conexion.commit()  
        return cursor.rowcount > 0 
    finally:
        cursor.close()
        conexion.close()

def delete_usuario(cursor, id):
    sql = "DELETE FROM usuarios WHERE id_usuario = %s"
    cursor.execute(sql, (id,))

    return cursor.rowcount
