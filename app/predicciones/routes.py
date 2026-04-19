from flask import Blueprint, request, jsonify
from app.predicciones import service
from app.utils.errors import ReturnErrors

predicciones_bp = Blueprint('predicciones', __name__)

# Registrar una predicción. --John
@predicciones_bp.route("/partidos/<int:id_partido>/prediccion", methods=["POST"])
def registrar_prediccion(id_partido):
    try:
        if id_partido <= 0:
            return jsonify(ReturnErrors(400)), 400

        data = request.get_json()
        if not data:
            return jsonify(ReturnErrors(400)), 400

        registered, code = service.registrar_prediccion(data, id_partido)

        if code in [400, 404, 409, 500]:
            return jsonify(ReturnErrors(code)), code

        return jsonify(registered), code

    except Exception as e:
        return jsonify(ReturnErrors(500)), 500
