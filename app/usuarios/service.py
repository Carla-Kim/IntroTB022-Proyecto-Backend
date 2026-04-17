from app.usuarios.model import eliminar_usuario_db

def eliminar_usuario_service(id_usuario):
   return eliminar_usuario_db(id_usuario)
