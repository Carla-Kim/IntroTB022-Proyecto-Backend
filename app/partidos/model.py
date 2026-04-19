from app.db import get_connection, get_cursor

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

def actualizar_resultado(gol_local_act,gol_visit_act, id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        sql = "UPDATE partidos SET goles_local = %s, goles_visitante = %s WHERE id_partido = %s"
        cursor.execute(sql, (gol_local_act, gol_visit_act, id))
        conn.commit()
        return cursor.rowcount  
    except Exception as e:
        conn.rollback() 
        raise e
    finally:
        cursor.close()
        conn.close()

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