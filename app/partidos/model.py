from app.db import get_connection
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
