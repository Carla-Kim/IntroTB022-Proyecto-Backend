from app.db import get_connection

def eliminar_usuario_db(id_usuario):
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute("""
          DELETE FROM usuarios WHERE id_usuario = %s"
   """, (id_usuario,))
   fila_eliminada = cursor.rowcount
   conn.commit()
   cursor.close()
   conn.close()
   return fila_eliminada > 0
