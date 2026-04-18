from app.schemas.primitives import EquipoSchema, FechaSchema, FaseSchema
from app.schemas.commons import PaginationSchema

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

ResultadoSchema = {
    "local": {"type": "integer", "min": 0},
    "visitante": {"type": "integer", "min": 0}
}