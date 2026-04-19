from flask import Flask
from app.config import *
from app.usuarios.routes import usuarios_bp
from app.partidos.routes import partidos_bp
from app.predicciones.routes import predicciones_bp
from app.ranking.routes import ranking_bp

print("INICIANDO APP")

validate_config()
app = Flask(__name__)

print("APP CREADA")

@app.route("/")
def home():
    return "OK"

print("RUTA / REGISTRADA")

app.json.sort_keys = False
app.register_blueprint(usuarios_bp)
app.register_blueprint(partidos_bp)
app.register_blueprint(predicciones_bp)
app.register_blueprint(ranking_bp)

print("BLUEPRINTS REGISTRADOS")

print(app.url_map)

if __name__ == "__main__":
    app.run(**APP_CONFIG)
