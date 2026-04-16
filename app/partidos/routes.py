from flask import Blueprint, jsonify
from app.partidos.service import borrar_partido_service

partidos_bp = Blueprint('partidos', __name__)

@partidos_bp.route('/partidos/<int:id_partido>', methods=['DELETE'])
def eliminar_partido(id_partido):
    fue_eliminado = borrar_partido_service(id_partido)
    
    if fue_eliminado:
        return jsonify({"mensaje": "Partido eliminado correctamente"}), 200
    
    return jsonify({"error": "El partido no existe"}), 404