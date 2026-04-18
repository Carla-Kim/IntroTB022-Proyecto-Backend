# from .model import COMPLETAR ACA CON LAS FUNCIONES DEL MODEL
from app.partido import model
from app.db import get_connection
from app.partidos.model import Partido
from app.utils.pagination import build_links

def actualizando_resultado(data,id_partido):
    gol_local = data.get("gol local")
    gol_visitante = data.get("gol visitante")
    gol_actualizado = model.actualizar_resultado(gol_local,gol_visitante, id_partido)
    
    if gol_actualizado == 0:
        return {
            "proceso" : "fallido",
            "mensaje" : f"No se encontro el ID del partido {id_partido} o el resultado ya fue actualizado"
        }, 404
    return {
        "proceso" : "existoso",
        "mensaje" : f"el partido {id_partido} actualizado {gol_local}-{gol_visitante}  "
    }, 200


class PartidoService:
    @staticmethod
    def get_partidos_paginados(limit, offset, equipo=None, fecha=None, fase=None):
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

        #Esto es para el HATEOAS
        query_count = f"SELECT COUNT(*) AS count FROM partidos {filters}"
        cursor.execute(query_count, params)
        total = cursor.fetchone()["count"]


        query_elems = f"""
            SELECT id_partido, equipo_local, equipo_visitante, fecha, fase, goles_local, goles_visitante 
            FROM partidos {filters} 
            LIMIT %s OFFSET %s
        """

        #aAplicamos los limits/offsets que nos indican.
        params_elems = params + [limit, offset]
        cursor.execute(query_elems, params_elems)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        partidos = []
        for row in rows:
            p = Partido(
                id_partido=row['id_partido'],
                local=row['equipo_local'],
                visitante=row['equipo_visitante'],
                fecha=row['fecha'],
                fase=row['fase'],
                goles_local=row['goles_local'],
                goles_visitante=row['goles_visitante']
            )
            partidos.append(p.to_dict())

        return {"items": partidos, "total": total}
    
    @staticmethod
    def get_partido_by_id(partido_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM partidos WHERE id_partido = %s"
        cursor.execute(query, (partido_id,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if not row:
            return None #Si lo dejamos con None, nos da un error 404. Hay que armar el asunto de los errores globales.

        partido_obj = Partido(
            id_partido=row['id_partido'],
            local=row['equipo_local'],
            visitante=row['equipo_visitante'],
            fecha=row['fecha'],
            fase=row['fase'],
            goles_local=row['goles_local'],
            goles_visitante=row['goles_visitante']
        )
        
        return partido_obj.to_dict()


class PartidosService:

    @staticmethod
    def listar_partidos(base_url, args, equipo=None, fecha=None, fase=None, limit=10, offset=0):
        data = PartidosModel.fetch_partidos(equipo, fecha, fase, limit, offset)

        partidos = [
            {
                "id": d["id_partido"],
                "equipo_local": d["equipo_local"],
                "equipo_visitante": d["equipo_visitante"],
                "fecha": str(d["fecha"]),
                "fase": d["fase"]
            }
            for d in data["rows"]
        ]

        count = data["count"]

        return {
          "partidos": partidos,
          "_links": build_links(base_url, args, limit, offset, count)
        }
