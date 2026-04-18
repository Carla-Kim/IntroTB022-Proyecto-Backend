from flask import Blueprint, request, jsonify
from app.partidos.service import get_partido_by_id
from app.utils.errors import BadRequestError
from app.utils.validations import validate
from app.partido import service

partidos_bp = Blueprint('partidos', __name__)

#Enpoints

@partidos_bp.route("/partidos/<int:id_partido>/resultado", methods=["PUT"])
def actualizando(id_partido):
    data = request.get_json()
    actualizado, code = service.actualizando_resultado(data, id_partido)
    return jsonify(actualizado), code
#rutas
@partidos_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def get_partido(partido_id):
    partido = get_partido_by_id(partido_id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404
   
    return jsonify(partido), 200
    #Por ahora dejamos los errores "armados a mano". Hay que armar los errores bien detallados para el usuario.

@partidos_bp.get("/partidos")
def listar_partidos():
    equipo = request.args.get("equipo")
    fecha = request.args.get("fecha")
    fase = request.args.get("fase")
    limit = request.args.get("_limit", type=int, default=10)
    offset = request.args.get("_offset", type=int, default=0)

    errors = validate_pagination(limit, offset)

    if errors:
        raise BadRequestError(errors=errors)

    base_url = request.base_url
    args = {
        k: v for k, v in {
            "equipo": equipo,
            "fecha": fecha,
            "fase": fase
        }.items() if v is not None
    }

    result = PartidosService.listar_partidos(
        equipo=equipo,
        fecha=fecha,
        fase=fase,
        limit=limit,
        offset=offset,
        base_url=base_url,
        args=args
    )

    return jsonify(result), 200
