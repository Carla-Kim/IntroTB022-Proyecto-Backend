from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from app.usuarios.service import crear_usuario_service

usuarios_bp = Blueprint('usuarios', __name__)

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