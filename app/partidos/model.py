def check_by_id(cursor, id):
    cursor.execute("SELECT 1 FROM partidos WHERE id_partido = %s", (id,))
    return cursor.fetchone() is not None

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

def fetch_partido(cursor, id):
    sql = "SELECT * FROM partidos WHERE id_partido = %s"
    cursor.execute(sql, (id,))

    return cursor.fetchone()

def update_partido(cursor, columns, params):
        sql = f"UPDATE partidos SET {', '.join(columns)} WHERE id_partido = %s"
        cursor.execute(sql, params)

def delete_partido(cursor, id):
    sql = "DELETE FROM partidos WHERE id_partido = %s"
    cursor.execute(sql, (id,))

    return cursor.rowcount

def update_resultado(cursor, id, goles_local, goles_visitante):
    sql = "UPDATE partidos SET goles_local = %s, goles_visitante = %s WHERE id_partido = %s"
    cursor.execute(sql, (goles_local, goles_visitante, id))

    return cursor.rowcount
