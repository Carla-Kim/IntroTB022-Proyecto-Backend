from app.usuarios.model import insertar_usuario, buscar_usuario_por_email, obtener_usuario_por_id


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
    
    # Actualizamos los datos del usuario
    usuario_existente["nombre"] = nuevo_nombre
    usuario_existente["email"] = nuevo_email
    
    return usuario_existente

