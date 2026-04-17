from flask import Blueprint, request, jsonify
from app.usuarios.service import eliminar_usuario_service

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
