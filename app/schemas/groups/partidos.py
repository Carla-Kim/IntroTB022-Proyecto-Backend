from app.schemas.primitives import IdSchema, EquipoSchema, FechaSchema, FaseSchema
from app.schemas.commons import PaginationSchema

ResultadoSchema = {
    "goles_local": {"type": "integer", "min": 0},
    "goles_visitante": {"type": "integer", "min": 0}
}

PartidosQuerySchema = {
    "equipo": EquipoSchema,
    "fecha": FechaSchema,
    "fase": FaseSchema,
    **PaginationSchema
}

PartidoBodySchema = {
    "fields": {
        "equipo_local": EquipoSchema,
        "equipo_visitante": EquipoSchema,
        "fecha": FechaSchema,
        "fase": FaseSchema,
    },
    "required": ["equipo_local", "equipo_visitante", "fecha", "fase"]
}

PartidoUpdateSchema = {
    "equipo_local": EquipoSchema,
    "equipo_visitante": EquipoSchema,
    "fecha": FechaSchema,
    "fase": FaseSchema,
}

PrediccionBodySchema = {
    "id_usuario": IdSchema,
    "id_partido": IdSchema,
    **ResultadoSchema
}
