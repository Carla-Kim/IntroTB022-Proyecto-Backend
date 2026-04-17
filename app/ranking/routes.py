from flask import Blueprint, request, jsonify
from app.ranking.service import obtener_ranking_service

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/ranking', methods=['GET'])
def obtener_ranking():
  try:
   limit = request.args.get('_limit', default=10, type=int)
   offset = request.args.get('_offset', default=0, type=int)
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
     return jsonify({"mensaje": "Error interno del servidor"}), 500
