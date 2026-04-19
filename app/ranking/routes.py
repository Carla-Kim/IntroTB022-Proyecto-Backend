from flask import Blueprint, request, jsonify
from app.ranking import service

ranking_bp = Blueprint("ranking", __name__)

# Listar ranking. --Nicolás
@ranking_bp.route('/ranking', methods=['GET'])
def listar_ranking():
    base_url = request.base_url
    limit = request.args.get("_limit", default=10, type=int)
    offset = request.args.get("_offset", default=0, type=int)

    results, code = service.listar_ranking(base_url, limit, offset)

    if code == 204:
        return "", code

    return jsonify(results), code
