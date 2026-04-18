from flask import Blueprint, request, jsonify
from app.usuarios.service import eliminar_usuario_service
from app.usuarios.service import crear_usuario_service, reemplazar_usuario_id

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
 try:
    fue_eliminado = eliminar_usuario_service(id_usuario)
    if fue_eliminado:
       return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200

    return jsonify({"mensaje": "No existe ese usuario"}), 404
 
 except Exception as e:
       return jsonify({"mensaje": "Error interno del servidor"}), 500

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


