# from .model import COMPLETAR ACA CON LAS FUNCIONES DEL MODEL
from app.partido import model
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
