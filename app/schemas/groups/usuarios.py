from app.schemas.primitives import IdSchema, NombreSchema, EmailSchema
from app.schemas.commons import PaginationSchema

UsuariosQuerySchema = {
    **PaginationSchema
}

UsuarioBodySchema = {
    "id": IdSchema,
    "nombre": NombreSchema,
    "email": EmailSchema
}
