from app.usuarios.model import insertar_usuario, buscar_usuario_por_email

def crear_usuario_service(nombre, email):
    # Validamos si el email ya existe para evitar errores de duplicados
    usuario_existente = buscar_usuario_por_email(email)
    if usuario_existente:
        return {"error": "Este email ya está registrado"}
    
    # Si no existe, lo creamos
    return insertar_usuario(nombre, email)