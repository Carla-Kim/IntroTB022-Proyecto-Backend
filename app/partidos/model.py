from app.db import get_connection

class PartidosModel:

    @staticmethod
    def fetch_partidos(equipo, fecha, fase, limit, offset):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        filters = "WHERE 1=1"
        params = []

        if equipo:
            filters += " AND (equipo_local = %s OR equipo_visitante = %s)"
            params.extend([equipo, equipo])

        if fecha:
            filters += " AND fecha = %s"
            params.append(fecha)

        if fase:
            filters += " AND fase = %s"
            params.append(fase)

        params_count = params.copy()
        params_elems = params.copy()

        params_elems.extend([limit, offset])

        query_count = f"SELECT COUNT(*) AS count FROM partidos {filters}"
        query_elems = f"SELECT id_partido, equipo_local, equipo_visitante, fecha, fase FROM partidos {filters} LIMIT %s OFFSET %s"
        
        cursor.execute(query_count, params_count)
        count = cursor.fetchone()["count"]

        cursor.execute(query_elems, params_elems)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "rows": rows,
            "count": count
        }