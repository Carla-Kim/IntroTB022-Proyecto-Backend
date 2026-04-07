# Architectura en capa
## ¿Qué es la arquitectura en capas?
La arquitectura en capas es una forma de organizar el código de una aplicación separando las responsabilidades en distintos niveles. Cada capa cumple una función específica y se comunica con la capa siguiente, evitando que todo quede mezclado.

## ¿Cómo decidimos utilizarlo?
Se adoptó una organización basada en capas utilizando las carpetas routes, services y models para separar responsabilidades dentro del sistema. Estas forman parte de las convenciones normalmente utilizadas. 
- routes: encargadas de recibir y manejar las solicitudes HTTP y construir las respuestas (códigos HTTP).
- service: contienen la lógica de negocio y coordinan las operaciones del sistema. Busca validar y utilizan las funciones implementadas en models para interactuar con la base de datos.  
- model: se implementan las funciones relacionadas con la base de datos.
- utils: todas las herramientas utilizadas recurrentemente, en este caso, la paginación (ej paginacion(datos, page, limit), filtra y devuelve solo los registros de la página solicitada), la validación de datos (ej validarEmail(email), comprueba que el email tenga un formato correcto) y el manejo de errores (ej manejarErrores(err), devuelve un mensaje y código HTTP adecuado). 

## Esquema del flujo de una arquitectura en capas
- Cliente: Realiza la solicitud HTTP POST /usuarios con los datos del usuario que desea crear.
- routes (crear_usuario): Recibe la solicitud. Con utils, verifica y valida que los datos básicos estén presentes (por ejemplo, email y contraseña) y la envía a la capa de servicios. 
- service (crear_usuario): Aplica la lógica de negocio: comprueba que no exista un usuario con los mismos datos, que el email tenga la estructura apropiada y prepara la información para la base de datos.
- model (insertar_usuario): Inserta el usuario en la base de datos y devuelve el resultado de la operación.
- Respuesta: Envía al cliente, a través de route, un HTTP confirmando que el usuario fue creado correctamente.
