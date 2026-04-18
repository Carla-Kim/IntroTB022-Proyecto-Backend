from app.db import get_connection
from app.partidos.model import formatear_partido

def get_partidos_paginados(limit, offset, equipo=None, fecha=None, fase=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
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

    query_count = f"SELECT COUNT(*) AS count FROM partidos {filters}"
    cursor.execute(query_count, params)
    total = cursor.fetchone()["count"]

    query_elems = f"""
        SELECT id_partido, equipo_local, equipo_visitante, fecha, fase, goles_local, goles_visitante 
        FROM partidos {filters} 
        LIMIT %s OFFSET %s
    """
    params_elems = params + [limit, offset]
    cursor.execute(query_elems, params_elems)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    partidos = []
    for row in rows:
        p_dict = formatear_partido(
            id_partido=row['id_partido'],
            local=row['equipo_local'],
            visitante=row['equipo_visitante'],
            fecha=row['fecha'],
            fase=row['fase'],
            goles_local=row['goles_local'],
            goles_visitante=row['goles_visitante']
        )
        partidos.append(p_dict)

    return {"items": partidos, "total": total}

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

    return formatear_partido(
        id_partido=row['id_partido'],
        local=row['equipo_local'],
        visitante=row['equipo_visitante'],
        fecha=row['fecha'],
        fase=row['fase'],
        goles_local=row['goles_local'],
        goles_visitante=row['goles_visitante']
    )