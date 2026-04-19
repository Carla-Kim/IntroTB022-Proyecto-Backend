from flask import Blueprint, request, jsonify
from app.predicciones import service

predicciones_bp = Blueprint('predicciones', __name__)

# Registrar una predicción. --John
@predicciones_bp.route("/partidos/<int:id_partido>/prediccion", methods=["POST"])
def registrar_prediccion(id_partido):
    data = request.get_json()
    registered, code = service.registrar_prediccion(data, id_partido)

    return jsonify(registered), code
