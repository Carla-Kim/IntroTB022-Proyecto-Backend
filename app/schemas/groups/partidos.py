from app.schemas.primitives import EquipoSchema, FechaSchema, FaseSchema
from app.schemas.pagination import PaginationSchema

PartidosQuerySchema = {
    "equipo": EquipoSchema,
    "fecha": FechaSchema,
    "fase": FaseSchema,
    **PaginationSchema
}

PartidoBaseSchema = {
    "fields": {
        "equipo_local": EquipoSchema,
        "equipo_visitante": EquipoSchema,
        "fecha": FechaSchema,
        "fase": FaseSchema,
    },
    "required": ["equipo_local", "equipo_visitante"]
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