# from .model import COMPLETAR ACA CON LAS FUNCIONES DEL MODEL
from app.prediccion import model
def guardar_prediccion(data, id_partido):
    id_usuario = data.get("id usuario")
    goles_locales = data.get("local")
    goles_visitantes = data.get("visitante")
    
    if id_usuario is None or goles_locales is None or goles_visitantes is None:
        return "solicitud incompleta"
    
    partido_valido = model.verificacion(id_partido)
    if partido_valido is None:
        return "no encontrado"
    try:
        id_prediccion = model.guardando_prediccion(id_usuario, id_partido, goles_locales, goles_visitantes)   
        return {
            "proceso": "existoso",
            "mensaje": "prediccion guardada correctamente",
            "id_usuario": id_prediccion
        }
    except Exception as e:
        if "Duplicate entry" in str(e):
            return "conflicto"
        raise e
