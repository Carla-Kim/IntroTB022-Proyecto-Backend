from app.usuarios.model import insertar_usuario, buscar_usuario_por_email, obtener_usuario_por_id, actualizar_usuario_db, eliminar_usuario_db, obtener_usuarios

def eliminar_usuario_service(id_usuario):
   return eliminar_usuario_db(id_usuario)

def crear_usuario_service(nombre, email):
    # Validamos si el email ya existe para evitar errores de duplicados
    usuario_existente = buscar_usuario_por_email(email)
    if usuario_existente:
        return {"error": "Este email ya está registrado"}
    
    # Si no existe, lo creamos
    return insertar_usuario(nombre, email)

def reemplazar_usuario_id(id_usuario, nuevo_nombre, nuevo_email):
    usuario_existente = obtener_usuario_por_id(id_usuario)
    if not usuario_existente:  
        return {"error": "Usuario no encontrado"}
    
    actualizar_usuario_db(id_usuario, nuevo_nombre, nuevo_email)

    return {
        "id_usuario": id_usuario, 
        "nombre": nuevo_nombre, 
        "email": nuevo_email
    }

def listar_usuarios_service():
    return obtener_usuarios()

def obtener_usuario_id_service(id_usuario):
    return obtener_usuario_id(id_usuario)