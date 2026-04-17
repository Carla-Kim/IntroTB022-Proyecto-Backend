from app.db import get_connection

def obtener_ranking(id_usuario, puntos):
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)
  cursor.execute("""
    SELECT 
        pred.id_usuario,
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
        ) AS puntos
    FROM predicciones pred
    JOIN partidos part ON pred.id_partido = part.id_partido
    GROUP BY pred.id_usuario
    ORDER BY puntos DESC
    LIMIT %s OFFSET %s
  """, )
  ranking = cursor.fetchall()
  cursor.close()
  conn.close()
return ranking
