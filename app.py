from flask import Flask
from app.config import Config
from app.usuarios.routes import usuarios_bp
from app.partidos.routes import partidos_bp
from app.prediccion.routes import prediccion_bp
from app.ranking.routes import ranking_bp

Config.validate()

app = Flask(__name__)

app.register_blueprint(usuarios_bp)
app.register_blueprint(partidos_bp)
app.register_blueprint(prediccion_bp)
app.register_blueprint(ranking_bp)

if __name__ == "__main__":
    app.run(port=Config.PORT, debug=Config.DEBUG)
