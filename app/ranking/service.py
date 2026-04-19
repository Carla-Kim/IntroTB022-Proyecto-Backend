from app.ranking import model
from app.db import get_cursor
from app.utils.errors import ReturnErrors
from app.utils.pagination import build_links
from app.utils.validations import validate_schema
from app.schemas.commons import PaginationSchema
from flask import jsonify

def listar_ranking(base_url, limit, offset):
    schema_errors = validate_schema(
        PaginationSchema,
        limit=limit,
        offset=offset
    )
    if schema_errors:
        return jsonify(ReturnErrors(400)), 400
    
    try:
        with get_cursor() as cursor:
            data = model.fetch_ranking(cursor, limit, offset)
    except Exception as e:
        return jsonify(ReturnErrors(500)), 500
    
    ranking = [{
        "id_usuario": d["id_usuario"],
        "puntos": d["puntos"]
    } for d in data["rows"] ]

    count = data["count"]
    
    if count == 0:
        return "", 204

    return {
        "ranking": ranking,
        "_links": build_links(base_url, {}, limit, offset, count)
    }, 200
