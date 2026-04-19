from flask import Blueprint, request, jsonify
from app.partidos import service
from app.utils import ReturnErrors

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

#Reemplazar un partido por ID.
@partidos_bp.route('/partidos/<int:id>', methods=['PUT'])
def put_partido(id):
    data = request.json
    
    campos_req = ['equipo_local', 'equipo_visitante', 'fecha', 'fase']
    if not all(k in data for k in campos_req):
        return jsonify(ReturnErrors({
            "code": "400",
            "message": "Bad Request",
            "level": "error",
            "description": "Faltan campos obligatorios en el body"
        })), 400
        
    res = service.servicio_reemplazar(id, data)
    
    if res["exito"]:
        return '', 204
    
    if res["error"]:
        return jsonify(ReturnErrors({
            "code": "500",
            "message": "Database Error",
            "level": "error",
            "description": res["error"]
        })), 500
    
    return jsonify(ReturnErrors({
        "code": "404",
        "message": "Not Found",
        "level": "error",
        "description": f"No existe el partido con ID {id}"
    })), 404


# Actualizar parcialmente un partido por ID.
@partidos_bp.route('/partidos/<int:id>', methods=['PATCH'])
def patch_partido(id):
    data = request.json
    
    if not data:
        return jsonify(ReturnErrors({
            "code": "400",
            "message": "Bad Request",
            "level": "error",
            "description": "No se proporcionaron datos para actualizar"
        })), 400
        
    if service.servicio_parchear(id, data):
        return '', 204
    
    return jsonify(ReturnErrors({
        "code": "404",
        "message": "Not Found",
        "level": "error",
        "description": f"No existe el partido con ID {id}"
    })), 404

# Actualizar resultados de un partido por ID.
@partidos_bp.route("/partidos/<int:id_partido>/resultado", methods=["PUT"])
def actualizando(id_partido):
    try:
        data = request.get_json()
        actualizado = service.actualizando_resultado(data, id_partido)
        if actualizado is None:
            return jsonify({"error": "No se encontró el ID del partido"}), 404
        return "", 204
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Datos inválidos o incompletos"}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500
    
