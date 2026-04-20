from flask import Blueprint, request, jsonify
from app.usuarios import service

usuarios_bp = Blueprint("usuarios", __name__)

# Listar usuarios. --Flor
@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    base_url = request.base_url
    limit = request.args.get("_limit", type=int, default=10)
    offset = request.args.get("_offset", type=int, default=0)

    if not listado:
        return '', 204
    return jsonify({"usuarios": listado}), 200
 
 except Exception as e:
    return jsonify(ReturnErrors(500)), 500
    results, code = service.listar_usuarios(base_url, limit, offset)

    if code == 204:
        return "", code

    return jsonify(results), code

# Crear usuario. --Neithan
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    added, code = service.crear_usuario(data)

    return jsonify(added), code

# Obtener un usuario por ID. --Flor
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario_id(id_usuario):
    try:
       usuario = service.obtener_usuario_id_service(id_usuario)
       
       if usuario is None:
          return jsonify(ReturnErrors(404)), 404
       
       return jsonify(usuario), 200
    
    except Exception as e:
       return jsonify(ReturnErrors(500))

# Reemplazar un usuario por ID. --Kevin
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def reemplazar_usuario(id):
    data = request.get_json()
    updated, code = service.reemplazar_usuario(data, id)
    
    if not data or 'nombre' not in data or 'email' not in data:
        return jsonify(ReturnErrors(400)), 400
    
    resultado = service.reemplazar_usuario_id(id_usuario, data['nombre'], data['email'])
    
    if "error" in resultado:
        return jsonify(ReturnErrors(404)), 404
    
    return jsonify(resultado), 200

# Eliminar un usuario. --Nicolás
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    try:
        if id_usuario <= 0:
            return jsonify(ReturnErrors(400)), 400
        
        fue_eliminado = service.eliminar_usuario_service(id_usuario)
     
        if fue_eliminado:
            return '', 204

        return jsonify(ReturnErrors(404)), 404
 
    except Exception as e:
        return jsonify(ReturnErrors(500)), 500
