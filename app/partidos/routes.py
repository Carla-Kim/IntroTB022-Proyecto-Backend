from flask import Blueprint, request, jsonify
from app.partidos import service
from app.utils.errors import ReturnErrors

partidos_bp = Blueprint("partidos", __name__)

# Listar y/o filtrar partidos. --Luis
@partidos_bp.route("/partidos", methods=["GET"])
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
@partidos_bp.route("/partidos", methods=["POST"])
def crear_partido():
    data = request.get_json()
    added, code = service.crear_partido(data)

    return jsonify(added), code

# Obtener un partido por ID. --Kevin
@partidos_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def get_partido(partido_id):
    partido = service.get_partido_by_id(partido_id)

    if not partido:
        return jsonify(ReturnErrors(404)), 404
   
    return jsonify(partido), 200

# Reemplazar un partido por ID. --Carla
@partidos_bp.route('/partidos/<int:id>', methods=['PUT'])
def put_partido(id):
    data = request.json
    
    campos_req = ['equipo_local', 'equipo_visitante', 'fecha', 'fase']
    if not all(k in data for k in campos_req):
        return jsonify(ReturnErrors(400)), 400
        
    res = service.servicio_reemplazar(id, data)
    
    if res["exito"]:
        return '', 204
    
    if res["error"]:
        return jsonify(ReturnErrors(500)), 500
    
    return jsonify(ReturnErrors(404)), 404


# Actualizar parcialmente un partido por ID. --Carla
@partidos_bp.route('/partidos/<int:id>', methods=['PATCH'])
def patch_partido(id):
    data = request.json
    
    if not data:
        return jsonify(ReturnErrors(400)), 400
        
    if service.servicio_parchear(id, data):
        return '', 204
    
    return jsonify(ReturnErrors(404)), 404

# Actualizar resultados de un partido por ID. --John
@partidos_bp.route("/partidos/<int:id>/resultado", methods=["PUT"])
def actualizar_resultado(id):
    data = request.get_json()
    updated, code = service.actualizar_resultado(data, id)

    if code == 204:
        return "", code

    return jsonify(updated), code
