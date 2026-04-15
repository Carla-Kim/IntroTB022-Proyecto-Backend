class Partido:
    def __init__(self, id_partido, local, visitante, fecha, fase, goles_local=None, goles_visitante=None):
        self.id = id_partido
        self.local = local
        self.visitante = visitante
        self.fecha = fecha
        self.fase = fase
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def to_dict(self):
        return {
            "id": self.id,
            "equipo_local": self.local,
            "equipo_visitante": self.visitante,
            "fecha": self.fecha.isoformat() if hasattr(self.fecha, 'isoformat') else str(self.fecha),
            "fase": self.fase,
            "resultado": {
                "goles_local": self.goles_local,
                "goles_visitante": self.goles_visitante
            } if self.goles_local is not None else None
        }