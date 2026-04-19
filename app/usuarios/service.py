from app.usuarios import model
from app.db import get_cursor
from app.utils.errors import ReturnErrors
from app.utils.pagination import build_links
from app.utils.validations import validate_schema
from app.schemas.groups.usuarios import *

def listar_usuarios_service():
    return model.obtener_usuarios()

def crear_usuario(data):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    nombre = data.get("nombre")
    email = data.get("email")
    
    if not nombre or not email:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    schema_errors = validate_schema(
        UsuarioBodySchema,
        nombre=nombre,
        email=email
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    try:
        with get_cursor() as cursor:
            exists_email = model.check_by_email(cursor, email)

            if exists_email:
                return ReturnErrors({
                    "code": "Err",
                    "message": "Err",
                    "level": "Err",
                    "description": "Err"
                }), 409

            new_id = model.insert_usuario(cursor, nombre, email)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500

    return {
        "id": new_id,
        "nombre": nombre,
        "email": email
    }, 201

def obtener_usuario_id_service(id_usuario):
    return model.obtener_usuario_id(id_usuario)

def reemplazar_usuario_id(id_usuario, nuevo_nombre, nuevo_email):
    usuario_existente = model.obtener_usuario_por_id(id_usuario)
    if not usuario_existente:  
        return {"error": "Usuario no encontrado"}
    
    model.actualizar_usuario_db(id_usuario, nuevo_nombre, nuevo_email)

    return {
        "id_usuario": id_usuario, 
        "nombre": nuevo_nombre, 
        "email": nuevo_email
    }

def eliminar_usuario(id):
    if id is None:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    schema_errors = validate_schema(IdSchema, id=id)
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    try:
        with get_cursor() as cursor:
            deleted = model.delete_usuario(cursor, id)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500
    
    if deleted == 0:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 404
    
    return "", 204
