from flask import Blueprint, request, jsonify
from app.partidos.service import PartidoService

partidos_bp = Blueprint('partidos', __name__)

#rutas
@partidos_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def get_partido(partido_id):
    partido = PartidoService.get_partido_by_id(partido_id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404
    
    return jsonify(partido), 200
    #Por ahora dejamos los errores "armados a mano". Hay que armar los errores bien detallados para el usuario.