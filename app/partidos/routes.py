from flask import Blueprint, request, jsonify
from app.partidos.service import PartidosService
from app.utils.errors import BadRequestError
from app.utils.validations import validate

partidos_bp = Blueprint('partidos', __name__)

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