# from .model import COMPLETAR ACA CON LAS FUNCIONES DEL MODEL
from app.db import get_connection, get_cursor
from app.partidos import model
from app.utils.errors import BadRequestError
from app.utils.pagination import build_links
from app.utils.validations import validate_schema
from app.schemas.groups.partidos import PartidosQuerySchema

def actualizando_resultado(data,id_partido):
    gol_local = data.get("gol local")
    gol_visitante = data.get("gol visitante")
    gol_actualizado = model.actualizar_resultado(gol_local,gol_visitante, id_partido)
    
    if gol_actualizado == 0:
        return {
            "proceso" : "fallido",
            "mensaje" : f"No se encontro el ID del partido {id_partido} o el resultado ya fue actualizado"
        }, 404
    return {
        "proceso" : "existoso",
        "mensaje" : f"el partido {id_partido} actualizado {gol_local}-{gol_visitante}  "
    }, 200

def listar_partidos(base_url, args, equipo=None, fecha=None, fase=None, limit=10, offset=0):
    errors = validate_schema(
        PartidosQuerySchema,
        equipo=equipo,
        fecha=fecha,
        fase=fase,
        limit=limit,
        offset=offset
    )
    
    if errors:
        raise BadRequestError(errors=errors)

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

    with get_cursor() as cursor:
        data = model.fetch_partidos(cursor, filters, params, limit, offset)

    partidos = [
        {
            "id": d["id_partido"],
            "equipo_local": d["equipo_local"],
            "equipo_visitante": d["equipo_visitante"],
            "fecha": str(d["fecha"]),
            "fase": d["fase"]
        }
        for d in data["rows"]
    ]

    count = data["count"]

    return {
        "partidos": partidos,
        "_links": build_links(base_url, args, limit, offset, count)
    }

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
