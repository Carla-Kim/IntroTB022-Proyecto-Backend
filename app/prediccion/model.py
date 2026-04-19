from app.db import get_connection
from app.db import get_connection
def verificacion(id_partido):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
      #verifica que el partido no se haya jugado aun 
        cursor.execute("SELECT id_partido FROM partidos WHERE id_partido = %s AND goles_local IS NULL", (id_partido,))
        return cursor.fetchone()
    
    finally:
        cursor.close()
        conn.close()
def guardando_prediccion(id_usuario, id_partido, goles_locales, goles_visitantes):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:        
        sql = "INSERT INTO predicciones (id_usuario, id_partido, goles_locales, goles_visitantes) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_usuario, id_partido, goles_locales, goles_visitantes))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
