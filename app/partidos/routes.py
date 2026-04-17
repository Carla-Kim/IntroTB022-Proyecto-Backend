from flask import Blueprint, request, jsonify
#from .service import COMPLETAR ACA CON LAS FUNCIONES DEL SERVICE

partidos_bp = Blueprint('partidos', __name__)

#Enpoints
from app.partido import service
@partidos_bp.route("/partidos/<int:id_partido>/resultado", methods=["PUT"])

def actualizando(id_partido):
    data = request.get_json()
    actualizado, code = service.actualizando_resultado(data, id_partido)
    return jsonify(actualizado), code
