from app.partidos.model import eliminar_partido_db

def borrar_partido_service(id_partido):
    return eliminar_partido_db(id_partido)