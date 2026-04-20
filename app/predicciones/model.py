def validar_prediccion(cursor, id_partido, id_usuario):
    sql = """
    SELECT 
        p.id_partido,
        p.goles_local,
        pr.id_usuario
    FROM partidos p
    LEFT JOIN predicciones pr 
        ON p.id_partido = pr.id_partido 
        AND pr.id_usuario = %s
    WHERE p.id_partido = %s
    """.strip()
    
    cursor.execute(sql, (id_usuario, id_partido))
    return cursor.fetchone()

def insert_prediccion(cursor, id_usuario, id_partido, goles_local, goles_visitante):
    sql = "INSERT INTO predicciones (id_usuario, id_partido, goles_local, goles_visitante) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (id_usuario, id_partido, goles_local, goles_visitante))
