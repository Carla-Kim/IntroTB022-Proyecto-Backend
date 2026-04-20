from flask import Blueprint, request, jsonify
from app.partidos import service

partidos_bp = Blueprint("partidos", __name__)

# Listar y/o filtrar partidos. --Luis
@partidos_bp.route('/partidos', methods=['GET'])
def listar_partidos():
    base_url = request.base_url
    args = request.args.to_dict()
    limit = request.args.get("_limit", type=int, default=10)
    offset = request.args.get("_offset", type=int, default=0)

    results, code = service.listar_partidos(base_url, args, limit, offset)

    if code == 204:
        return "", code

    return jsonify(results), code

# Crear un partido. --Luis
@partidos_bp.route('/partidos', methods=['POST'])
def crear_partido():
    data = request.get_json()
    added, code = service.crear_partido(data)

    return jsonify(added), code

# Obtener un partido por ID. --Kevin
@partidos_bp.route('/partidos/<int:id>', methods=['GET'])
def obtener_partido(id):
    result, code = service.obtener_partido(id)
   
    return jsonify(result), code

# Reemplazar un partido por ID. --Carla
@partidos_bp.route('/partidos/<int:id>', methods=['PUT'])
def reemplazar_partido(id):
    data = request.get_json()
    updated, code = service.reemplazar_partido(data, id)

    if code == 204:
        return "", code
    
    return jsonify(updated), code

# Actualizar parcialmente un partido por ID. --Carla
@partidos_bp.route('/partidos/<int:id>', methods=['PATCH'])
def actualizar_partido(id):
    data = request.get_json()    
    updated, code = service.actualizar_partido(data, id)

    if code == 204:
        return "", code
    
    return jsonify(updated), code

# Actualizar resultados de un partido por ID. --John
@partidos_bp.route('/partidos/<int:id>/resultado', methods=['PUT'])
def actualizar_resultado(id):
    data = request.get_json()
    updated, code = service.actualizar_resultado(data, id)

    if code == 204:
        return "", code

    return jsonify(updated), code
