from app.db import get_cursor
from app.predicciones import model
from app.utils.errors import ReturnErrors
from app.utils.validations import validate_schema
from app.schemas.groups.partidos import *

def registrar_prediccion(data, id_partido):
    if not data:
        return ReturnErrors(400), 400

    id_usuario = data.get("id_usuario")
    goles_local = data.get("goles_local")
    goles_visitante = data.get("goles_visitante")
    
    if id_usuario is None or goles_local is None or goles_visitante is None:
        return ReturnErrors(400), 400
    
    schema_errors = validate_schema(
        PrediccionBodySchema,
        id_usuario=id_usuario,
        goles_local=goles_local,
        goles_visitante=goles_visitante
    )
    if schema_errors:
        return ReturnErrors(400), 400
    
    try:
        with get_cursor() as cursor:
            validation = model.validar_prediccion(cursor, id_partido, id_usuario)

            if validation is None:
                return ReturnErrors(404), 404

            if validation.get("goles_local") is not None:
                return ReturnErrors(400), 400

            if validation.get("id_usuario") is not None:
                return ReturnErrors(409), 409

            model.insert_prediccion(cursor, id_usuario, id_partido, goles_local, goles_visitante)
    except Exception:
        return ReturnErrors(500), 500

    return {
        "id_usuario": id_usuario,
        "id_partido": id_partido,
        "goles_local": goles_local,
        "goles_visitante": goles_visitante
    }, 201
