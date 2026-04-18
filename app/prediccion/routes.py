from flask import Blueprint, request, jsonify
#from .service import COMPLETAR ACA CON LAS FUNCIONES DEL SERVICE

prediccion_bp = Blueprint('prediccion', __name__)

#Enpoints
from app.prediccion import service
@prediccion_bp.route("/partidos/<int:id_partido>/prediccion", methods=["POST"])
def guardar_prediccion(id_partido):
    data = request.get_json()
    resultado, code = service.guardar_prediccion(data, id_partido)
    return jsonify(resultado), code
