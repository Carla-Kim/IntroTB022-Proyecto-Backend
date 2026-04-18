from app.db import get_connection

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

def buscar_usuario_por_email(email):
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return usuario

def insertar_usuario(nombre, email):
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    cursor.execute(query, (nombre, email))
    nuevo_id = cursor.lastrowid
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"id_usuario": nuevo_id, "nombre": nombre, "email": email}

#N°8 Kevin
def obtener_usuario_por_id(id_usuario):
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        query = "SELECT * FROM usuarios WHERE id_usuario = %s"
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
