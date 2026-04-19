from flask import Blueprint, request, jsonify
from app.usuarios.service import eliminar_usuario_service, obtener_usuario_id_service, listar_usuarios_service, crear_usuario_service, reemplazar_usuario_id
from app.utils.errors import ReturnErrors

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    try:
       if id_usuario <= 0:
            return jsonify(ReturnErrors({
                "code": "400",
                "message": "Bad Request",
                "level": "error",
                "description": "El id_usuario no puede ser menor a 0"
            })), 400
        
       fue_eliminado = eliminar_usuario_service(id_usuario)
     
       if fue_eliminado:
          return '', 204

       return jsonify(ReturnErrors({
          "code": "404",
          "message": "Not Found",
          "level": "error",
          "description": "No existe ese usuario"
         })), 404
 
    except Exception as e:
         return jsonify(ReturnErrors({
            "code": "500",
            "message": "Database Error",
            "level": "error",
            "description": str(e)
        })), 500

@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    
    # Validamos que lleguen los datos
    if not data or 'nombre' not in data or 'email' not in data:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
        
    resultado = crear_usuario_service(data['nombre'], data['email'])
    
    if "error" in resultado:
        return jsonify(resultado), 400
        
    return jsonify(resultado), 201

@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def reemplazar_usuario(id_usuario):
    data = request.get_json()
    
    if not data or 'nombre' not in data or 'email' not in data:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    
    resultado = reemplazar_usuario_id(id_usuario, data['nombre'], data['email'])
    
    if "error" in resultado:
        return jsonify(resultado), 404
    
    return jsonify(resultado), 200

@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
 try:
    listado = listar_usuarios_service()

    if not listado:
        return '', 204
    return jsonify({"usuarios": listado}), 200
 
 except Exception as e:
    return jsonify({"mensaje": "Error interno del servidor"}), 500
 

@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario_id(id_usuario):
    try:
       usuario = obtener_usuario_id_service(id_usuario)
       
       if usuario is None:
          return jsonify({"mensaje": "Usuario no encontrado"}), 404
       return jsonify(usuario), 200
    
    except Exception as e:
       return jsonify({"mensaje": "Error interno del servidor"}), 500
