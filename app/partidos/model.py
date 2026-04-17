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
