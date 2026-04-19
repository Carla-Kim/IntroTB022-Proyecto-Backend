from app.db import get_connection, get_cursor
from app.partidos import model
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

def get_partido_by_id(partido_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM partidos WHERE id_partido = %s"
    cursor.execute(query, (partido_id,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return None 

    return model.formatear_partido(
        id_partido=row['id_partido'],
        local=row['equipo_local'],
        visitante=row['equipo_visitante'],
        fecha=row['fecha'],
        fase=row['fase'],
        goles_local=row['goles_local'],
        goles_visitante=row['goles_visitante']
    )

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
