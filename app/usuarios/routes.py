from flask import Blueprint, request, jsonify
from app.usuarios import service

usuarios_bp = Blueprint("usuarios", __name__)

# Listar usuarios. --Flor
@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    base_url = request.base_url
    limit = request.args.get("_limit", type=int, default=10)
    offset = request.args.get("_offset", type=int, default=0)

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
@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    result, code = service.obtener_usuario(id)

    return jsonify(result), code

# Reemplazar un usuario por ID. --Kevin
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def reemplazar_usuario(id):
    data = request.get_json()
    updated, code = service.reemplazar_usuario(data, id)
    
    if code == 204:
        return "", code

    return jsonify(updated), code

# Eliminar un usuario por ID. --Nicolás
@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    deleted, code = service.eliminar_usuario(id)
    
    if code == 204:
        return "", 204

    return jsonify(deleted), code
