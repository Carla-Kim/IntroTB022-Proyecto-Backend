def fetch_partidos(cursor, filters, params_count, params_elems):
    sql_count = f"SELECT COUNT(*) AS count FROM partidos {filters}"
    sql_elems = f"SELECT id_partido, equipo_local, equipo_visitante, fecha, fase FROM partidos {filters} LIMIT %s OFFSET %s"

    cursor.execute(sql_count, params_count)
    count = cursor.fetchone()["count"]

    cursor.execute(sql_elems, params_elems)
    rows = cursor.fetchall()

    return {
        "rows": rows,
        "count": count
    }

def insert_partido(cursor, equipo_local, equipo_visitante, fecha, fase):
    sql = "INSERT INTO partidos (equipo_local, equipo_visitante, fecha, fase) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (equipo_local, equipo_visitante, fecha, fase))

    return cursor.lastrowid

def formatear_partido(id_partido, local, visitante, fecha, fase, goles_local=None, goles_visitante=None):
    fecha_simple = str(fecha)

    resultado = None
    if goles_local is not None:
        resultado = {
            "goles_local": goles_local,
            "goles_visitante": goles_visitante
        }

    return {
        "id": id_partido,
        "equipo_local": local,
        "equipo_visitante": visitante,
        "fecha": fecha_simple,
        "fase": fase,
        "resultado": resultado
    }

def update_resultado(cursor, id, goles_local, goles_visitante):
    sql = "UPDATE partidos SET goles_local = %s, goles_visitante = %s WHERE id_partido = %s"
    cursor.execute(sql, (goles_local, goles_visitante, id))

    return cursor.rowcount
