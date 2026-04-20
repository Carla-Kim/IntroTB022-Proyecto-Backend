from app.usuarios import model
from app.db import get_cursor
from app.utils.errors import ReturnErrors
from app.utils.pagination import build_links
from app.utils.validations import validate_schema
from app.schemas.groups.usuarios import *

def listar_usuarios(base_url, limit, offset):
    schema_errors = validate_schema(
        PaginationSchema,
        limit=limit,
        offset=offset
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    try:
        with get_cursor() as cursor:
            data = model.fetch_usuarios(cursor, limit, offset)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500

    usuarios = [{
        "id": d["id_usuario"],
        "nombre": d["nombre"]
    } for d in data["rows"] ]

    count = data["count"]

    return {
        "usuarios": usuarios,
        "_links": build_links(base_url, {}, limit, offset, count)
    }, 200

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

def obtener_usuario(id):
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
            exists_id = model.check_by_id(cursor, id)

            if not exists_id:
                return ReturnErrors({
                "code": "Err",
                "message": "Err",
                "level": "Err",
                "description": "Err"
            }), 404

            result = model.fetch_usuario(cursor, id)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500
    
    usuario = {
        "id": result["id_usuario"],
        "nombre": result["nombre"],
        "email": result["email"]
    }
    
    return usuario, 200

def reemplazar_usuario(data, id):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    nombre = data.get("nombre")
    email = data.get("email")

    if not all([nombre, email]):
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    schema_errors = validate_schema(
        UsuarioBodySchema,
        id=id,
        nombre=nombre,
        email=email
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    try:
        with get_cursor() as cursor:
            exists_id = model.check_by_id(cursor, id)

            if not exists_id:
                return ReturnErrors({
                "code": "Err",
                "message": "Err",
                "level": "Err",
                "description": "Err"
            }), 404

            model.update_usuario(cursor, id, nombre, email)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500

    return "", 204

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
