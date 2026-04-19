from app.db import get_connection

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

def db_reemplazar_partido(id_partido, local, visitante, fecha, fase):
    conexion = None
    cursor = None

    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        
        query = """
            UPDATE partidos 
            SET equipo_local = %s, equipo_visitante = %s, fecha = %s, fase = %s
            WHERE id_partido = %s
        """
        cursor.execute(query, (local, visitante, fecha, fase, id_partido))

        filas = cursor.rowcount
        conexion.commit()
        
        return {"exito": filas > 0, "error": None}

    except Exception as e:
        if conexion: conexion.rollback()
        return {"exito": False, "error": str(e)}
    
    finally:
        if conexion: conexion.close()
        if cursor: cursor.close()

def db_actualizar_parcial(id_partido, datos_a_cambiar):
    if not datos_a_cambiar: return {"exito": False, "error": "No hay datos"}
    
    conexion = None
    cursor = None

    try:
        conexion = get_connection()
        cursor = conexion.cursor()

        campos = [f"{clave} = %s" for clave in datos_a_cambiar.keys()]
        valores = list(datos_a_cambiar.values())
        valores.append(id_partido)
        
        query = f"UPDATE partidos SET {', '.join(campos)} WHERE id_partido = %s"
        cursor.execute(query, tuple(valores))
        
        filas = cursor.rowcount
        conexion.commit()
        
        return {"exito": filas > 0, "error": None}

    except Exception as e:
        if conexion: conexion.rollback()
        return {"exito": False, "error": str(e)}
        
    finally:
        if conexion: conexion.close()
        if cursor: cursor.close()

def delete_partido(cursor, id):
    sql = "DELETE FROM partidos WHERE id_partido = %s"
    cursor.execute(sql, (id,))

    return cursor.rowcount

def update_resultado(cursor, id, goles_local, goles_visitante):
    sql = "UPDATE partidos SET goles_local = %s, goles_visitante = %s WHERE id_partido = %s"
    cursor.execute(sql, (goles_local, goles_visitante, id))

    return cursor.rowcount
