from app.ranking.model import obtener_ranking_db

def obtener_ranking_service(limit, offset):
  return obtener_ranking_db(limit, offset)
