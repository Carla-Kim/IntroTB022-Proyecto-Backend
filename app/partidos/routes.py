from flask import Blueprint, request, jsonify
from app.partidos.service import get_partido_by_id

partidos_bp = Blueprint('partidos', __name__)

@partidos_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def get_partido(partido_id):
    partido = get_partido_by_id(partido_id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404
    
    return jsonify(partido), 200