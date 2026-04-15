from app.partidos.model import PartidosModel
from app.utils.pagination import build_links

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