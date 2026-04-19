from app.partidos import model
from app.db import get_connection, get_cursor
from app.utils.errors import ReturnErrors
from app.utils.pagination import build_links
from app.utils.validations import validate_schema
from app.schemas.groups.partidos import *

def listar_partidos(base_url, args, limit, offset):
    equipo = args.get("equipo")
    fecha = args.get("fecha")
    fase = args.get("fase")

    schema_errors = validate_schema(
        PartidosQuerySchema,
        equipo=equipo,
        fecha=fecha,
        fase=fase,
        limit=limit,
        offset=offset
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    filters = "WHERE 1=1"
    params = []

    if equipo:
        filters += " AND (equipo_local = %s OR equipo_visitante = %s)"
        params.extend([equipo, equipo])
    if fecha:
        filters += " AND fecha = %s"
        params.append(fecha)
    if fase:
        filters += " AND fase = %s"
        params.append(fase)

    params_elems = [*params, limit, offset]
    params_count = params

    try:
        with get_cursor() as cursor:
            data = model.fetch_partidos(cursor, filters, params_count, params_elems)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500

    partidos = [{
        "id": d["id_partido"],
        "equipo_local": d["equipo_local"],
        "equipo_visitante": d["equipo_visitante"],
        "fecha": str(d["fecha"]),
        "fase": d["fase"]
    } for d in data["rows"] ]

    count = data["count"]

    return {
        "partidos": partidos,
        "_links": build_links(base_url, args, limit, offset, count)
    }, 200

def crear_partido(data):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    equipo_local = data.get("equipo_local")
    equipo_visitante = data.get("equipo_visitante")
    fecha = data.get("fecha")
    fase = data.get("fase")

    if not all([equipo_local, equipo_visitante, fecha, fase]):
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    schema_errors = validate_schema(
    PartidoBodySchema,
    equipo_local=equipo_local,
    equipo_visitante=equipo_visitante,
    fecha=fecha,
    fase=fase
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    if equipo_local == equipo_visitante:
        ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    try:
        with get_cursor() as cursor:
            new_id = model.insert_partido(cursor, equipo_local, equipo_visitante, fecha, fase)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500

    return {
        "id": new_id,
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "fecha": fecha,
        "fase": fase
    }, 201

def obtener_partido(id):
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

            result = model.fetch_partido(cursor, id)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500
    
    partido = {
        "id": result["id_partido"],
        "equipo_local": result["equipo_local"],
        "equipo_visitante": result["equipo_visitante"],
        "fecha": str(result["fecha"]),
        "fase": result["fase"],
        "resultado": {"local": result["goles_local"], "visitante": result["goles_visitante"]}
    }

    return partido, 200

def reemplazar_partido(data, id):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    equipo_local = data.get("equipo_local")
    equipo_visitante = data.get("equipo_visitante")
    fecha = data.get("fecha")
    fase = data.get("fase")

    if not all([equipo_local, equipo_visitante, fecha, fase]):
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    schema_errors = validate_schema(
        PartidoBodySchema,
        id=id,
        equipo_local=equipo_local,
        equipo_visitante=equipo_visitante,
        fecha=fecha,
        fase=fase
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    columns = [
        "equipo_local = %s",
        "equipo_visitante = %s",
        "fecha = %s",
        "fase = %s"
    ]
    params = [equipo_local, equipo_visitante, fecha, fase, id]

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

            model.update_partido(cursor, columns, params)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500
    
    return "", 204

def actualizar_partido(data, id):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    equipo_local = data.get("equipo_local")
    equipo_visitante = data.get("equipo_visitante")
    fecha = data.get("fecha")
    fase = data.get("fase")

    if not any([equipo_local, equipo_visitante, fecha, fase]):
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    schema_errors = validate_schema(
        PartidoUpdateSchema,
        id=id,
        equipo_local=equipo_local,
        equipo_visitante=equipo_visitante,
        fecha=fecha,
        fase=fase
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400

    columns = []
    params = []

    if equipo_local is not None:
        columns.append("equipo_local = %s")
        params.append(equipo_local)
    if equipo_visitante is not None:
        columns.append("equipo_visitante = %s")
        params.append(equipo_visitante)
    if fecha is not None:
        columns.append("fecha = %s")
        params.append(fecha)
    if fase is not None:
        columns.append("fase = %s")
        params.append(fase)

    params.append(id)

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

            model.update_partido(cursor, columns, params)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500
    
    return "", 204

def eliminar_partido(id):
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
            deleted = model.delete_partido(cursor, id)
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

def actualizar_resultado(data, id):
    if not data:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400

    goles_local = data.get("goles_local")
    goles_visitante = data.get("goles_visitante")

    if goles_local is None or goles_visitante is None:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 400
    
    schema_errors = validate_schema(
        ResultadoSchema,
        goles_local=goles_local,
        goles_visitante=goles_visitante
    )
    if schema_errors:
        return ReturnErrors(*schema_errors), 400
    
    try:
        with get_cursor() as cursor:
            updated = model.update_resultado(cursor, id, goles_local, goles_visitante)
    except Exception as e:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": str(e)
        }), 500
    
    if updated == 0:
        return ReturnErrors({
            "code": "Err",
            "message": "Err",
            "level": "Err",
            "description": "Err"
        }), 404
    
    return "", 204
