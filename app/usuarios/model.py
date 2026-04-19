from app.db import get_connection

def check_email(cursor, email):
    cursor.execute("SELECT 1 FROM usuarios WHERE email = %s", (email,))
    return cursor.fetchone() is not None

###

def obtener_usuarios():
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT id_usuario as id, nombre FROM usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios

def insert_usuario(cursor, nombre, email):
    sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    cursor.execute(sql, (nombre, email))

    return cursor.lastrowid

def obtener_usuario_por_id(id_usuario):
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        query = "SELECT id_usuario as id, nombre, email FROM usuarios WHERE id_usuario = %s"
        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone()
        if usuario:
            return usuario
        else:
            return None
    finally:
        cursor.close()
        conexion.close()

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

def eliminar_usuario_db(id_usuario):
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute("""
          DELETE FROM usuarios WHERE id_usuario = %s
   """, (id_usuario,))
   fila_eliminada = cursor.rowcount
   conn.commit()
   cursor.close()
   conn.close()
   return fila_eliminada > 0
