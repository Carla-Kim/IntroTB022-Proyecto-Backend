from flask import Blueprint, request, jsonify
from app.ranking.service import obtener_ranking_service
from app.utils.errors import ReturnErrors

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/ranking', methods=['GET'])
def obtener_ranking():
    try:
        limit = request.args.get('_limit', default=10, type=int)
        offset = request.args.get('_offset', default=0, type=int)
        if limit is None or offset is None or limit <= 0 or offset < 0:
            return jsonify(ReturnErrors({
                "code": "400",
                "message": "Bad Request",
                "level": "error",
                "description": "Los parámetros _limit y _offset no son validos"
            })), 400

        
        ranking = obtener_ranking_service(limit, offset)

        if not ranking:
          return '', 204
   
        base_url = "http://localhost:5000/ranking"
        response = {
            "ranking": ranking,
            "_links": {
                "_first": {"href": f"{base_url}?_offset=0&_limit={limit}"},
                "_prev": {"href": f"{base_url}?_offset={max(0, offset - limit)}&_limit={limit}"},
                "_next": {"href": f"{base_url}?_offset={offset + limit}&_limit={limit}"},
                "_last": {"href": f"{base_url}?_offset={offset}&_limit={limit}"} 
            }
        }
        return jsonify(response), 200
  
    except Exception as e:
         return jsonify(ReturnErrors({
            "code": "500",
            "message": "Internal Server Error",
            "level": "error",
            "description": str(e)
        })), 500
