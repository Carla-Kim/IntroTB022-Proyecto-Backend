from app.db import get_connection

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