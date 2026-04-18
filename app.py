from flask import Flask
from app.config import Config
from app.utils.errors import register_error_handlers
from app.usuarios.routes import usuarios_bp
from app.partidos.routes import partidos_bp
from app.prediccion.routes import prediccion_bp
from app.ranking.routes import ranking_bp

print("INICIANDO APP")

Config.validate()

app = Flask(__name__)

print("APP CREADA")

@app.route("/")
def home():
    return "OK"

print("RUTA / REGISTRADA")

register_error_handlers(app)
app.register_blueprint(usuarios_bp)
app.register_blueprint(partidos_bp)
app.register_blueprint(prediccion_bp)
app.register_blueprint(ranking_bp)

print("BLUEPRINTS REGISTRADOS")

print(app.url_map)

if __name__ == "__main__":
    app.run(port=5000, debug=True)