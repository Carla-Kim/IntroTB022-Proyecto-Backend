from flask import Blueprint, request, jsonify
from app.partidos import service

partidos_bp = Blueprint("partidos", __name__)

# Listar y/o filtrar partidos.
@partidos_bp.route("/partidos", methods=["GET"])
def listar_partidos():
    base_url = request.base_url
    args = request.args.to_dict()
    limit = request.args.get("_limit", type=int, default=10)
    offset = request.args.get("_offset", type=int, default=0)

    results, code = service.listar_partidos(base_url, args, limit, offset)

    return jsonify(results), code

# Crear un partido.
@partidos_bp.route("/partidos", methods=["POST"])
def crear_partido():
    data = request.get_json()
    added, code = service.crear_partido(data)

    return jsonify(added), code

# Obtener un partido por ID.
@partidos_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def get_partido(partido_id):
    partido = service.get_partido_by_id(partido_id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404
   
    return jsonify(partido), 200

# Actualizar resultados de un partido por ID.
@partidos_bp.route("/partidos/<int:id_partido>/resultado", methods=["PUT"])
def actualizando(id_partido):
    try:
        data = request.get_json()
        actualizado = service.actualizando_resultado(data, id_partido)
        if actualizado is None:
            return jsonify({"error": "No se encontró el ID del partido"}), 404
        return jsonify(actualizado), 200
    except Exception as e:
        return jsonify({"error": "Datos inválidos"}), 400
