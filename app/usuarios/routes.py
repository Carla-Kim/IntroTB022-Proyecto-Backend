from flask import Blueprint, request, jsonify
from app.usuarios import service
from app.utils.errors import ReturnErrors

usuarios_bp = Blueprint('usuarios', __name__)

# Listar usuarios. --Flor
@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
 try:
    listado = service.listar_usuarios_service()

    if not listado:
        return '', 204
    return jsonify({"usuarios": listado}), 200
 
 except Exception as e:
    return jsonify({"mensaje": "Error interno del servidor"}), ReturnErrors(500)

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
          return jsonify({"mensaje": "Usuario no encontrado"}), ReturnErrors(404)
       
       return jsonify(usuario), 200
    
    except Exception as e:
       return jsonify(ReturnErrors(500))

# Reemplazar un usuario por ID. --Kevin
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def reemplazar_usuario(id_usuario):
    data = request.get_json()
    
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
