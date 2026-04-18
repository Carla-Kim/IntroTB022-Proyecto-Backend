from flask import Blueprint, request, jsonify
#from .service import COMPLETAR ACA CON LAS FUNCIONES DEL SERVICE

prediccion_bp = Blueprint('prediccion', __name__)

#Enpoints
from app.prediccion import service
@prediccion_bp.route("/partidos/<int:id_partido>/prediccion", methods=["POST"])
def guardar_prediccion(id_partido):
    try:
        data = request.get_json()
        resultado = service.guardar_prediccion(data, id_partido)
        if resultado is None:
            return jsonify({"error": "El partido ya se jugó o no existe. No podés predecir."}), 400
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
