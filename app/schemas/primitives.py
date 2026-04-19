IdSchema = {
    "type": "integer",
    "min": 1
}

EquipoSchema = {
    "type": "string"
}

FechaSchema = {
    "type": "string",
    "format": "date"
}

FaseSchema = {
    "type": "string",
    "enum": ["grupos", "dieciseisavos", "octavos", "cuartos", "semis", "final"]
}