# from .model import COMPLETAR ACA CON LAS FUNCIONES DEL MODEL
from app.prediccion import model
def guardar_prediccion(data, id_partido):
    id_usuario = data.get("id usuario")
    goles_locales = data.get("local")
    goles_visitantes = data.get("visitante")
    
    partido_valido = model.verificacion(id_partido)
    if partido_valido is None:
        return {
            "error": "El partido ya se jugó o no existe. No podés predecir."
        }, 404 
    try:
        id_prediccion = model.guardando_prediccion(id_usuario, id_partido, goles_locales, goles_visitantes)   

        return {
            "proceso": "existoso",
            "mensaje": "prediccion guardada correctamente",
            "id_usuario": id_prediccion
    }, 201
    except Exception as e:
        return {
            "error": str(e)
        }, 500
