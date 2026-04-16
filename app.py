from flask import Flask
from app.config import Config
from app.usuarios.routes import usuarios_bp
from app.partidos.routes import partidos_bp

print("INICIANDO APP")

Config.validate()

app = Flask(__name__)

print("APP CREADA")

@app.route("/")
def home():
    return "OK"

print("RUTA / REGISTRADA")

app.register_blueprint(usuarios_bp)
app.register_blueprint(partidos_bp)

print("BLUEPRINTS REGISTRADOS")

print(app.url_map)

if __name__ == "__main__":
    app.run(port=5000, debug=True)