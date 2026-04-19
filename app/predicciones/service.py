from app.db import get_cursor
from app.predicciones import model
from app.utils.errors import ReturnErrors
from app.utils.validations import validate_schema
from app.schemas.groups.partidos import *

def registrar_prediccion(data, id_partido):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    id_usuario = data.get("id_usuario")
    goles_local = data.get("goles_local")
    goles_visitante = data.get("goles_visitante")
    
    if id_usuario is None or goles_local is None or goles_visitante is None:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    schema_errors = validate_schema(
        PrediccionBodySchema,
        id_usuario=id_usuario,
        goles_local=goles_local,
        goles_visitante=goles_visitante
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400
    
    try:
        with get_cursor() as cursor:
            validation = model.validar_prediccion(cursor, id_partido, id_usuario)

        if validation is None:
            return ReturnErrors({
                "code": "Err",
                "message": "Err",
                "level": "Err",
                "description": "Err"
            }), 404

        if validation["goles_local"] is not None:
            return ReturnErrors({
                "code": "Err",
                "message": "Err",
                "level": "Err",
                "description": "Err"
            }), 400

        if validation["id_usuario"] is not None:
            return ReturnErrors({
                "code": "Err",
                "message": "Err",
                "level": "Err",
                "description": "Err"
            }), 409

        with get_cursor() as cursor:
            model.insert_prediccion(cursor, id_usuario, id_partido, goles_local, goles_visitante)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500

    return {
        "id_usuario": id_usuario,
        "id_partido": id_partido,
        "goles_local": goles_local,
        "goles_visitante": goles_visitante
    }, 201
