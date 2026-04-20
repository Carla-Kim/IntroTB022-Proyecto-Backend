def fetch_ranking(cursor, limit, offset):
    sql_count = "SELECT COUNT(*) AS count FROM usuarios"
    sql_elems = """
        SELECT 
            usua.id_usuario,
            COALESCE(
                SUM(
                    CASE
                        WHEN pred.goles_local = part.goles_local 
                            AND pred.goles_visitante = part.goles_visitante 
                            THEN 3

                        WHEN 
                            (pred.goles_local > pred.goles_visitante AND part.goles_local > part.goles_visitante)
                            OR
                            (pred.goles_local < pred.goles_visitante AND part.goles_local < part.goles_visitante)
                            OR
                            (pred.goles_local = pred.goles_visitante AND part.goles_local = part.goles_visitante)
                            THEN 1

                        ELSE 0
                    END
                ),
                0
            ) AS puntos
        FROM usuarios usua
        LEFT JOIN predicciones pred ON usua.id_usuario = pred.id_usuario
        LEFT JOIN partidos part
        ON pred.id_partido = part.id_partido
        WHERE part.goles_local IS NOT NULL
        AND part.goles_visitante IS NOT NULL
        GROUP BY usua.id_usuario
        ORDER BY puntos DESC, usua.id_usuario ASC
        LIMIT %s OFFSET %s
    """.strip()

    cursor.execute(sql_count)
    count = cursor.fetchone()["count"]

    cursor.execute(sql_elems, (limit, offset))
    rows = cursor.fetchall()

    return {
        "rows": rows,
        "count": count
    }
