from app.db import get_connection

def eliminar_partido_db(id_partido):
    conexion = get_connection()
    cursor = conexion.cursor()
    query = "DELETE FROM partidos WHERE id_partido = %s"
    cursor.execute(query, (id_partido,))
    filas_afectadas = cursor.rowcount
    conexion.commit()
    cursor.close()
    conexion.close()
    return filas_afectadas > 0