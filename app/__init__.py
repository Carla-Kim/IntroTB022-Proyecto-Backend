from flask import Flask
from app.usuarios.routes import usuarios_bp

def create_app():
    app = Flask(__name__)
    
    # Registro del blueprint
    app.register_blueprint(usuarios_bp)
    
    return app