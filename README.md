# Introducción al Desarrollo de Software: Proyecto Backend 
- Información del curso: Universidad de Buenos Aires, Curso Lanzillotta, 1C2026.
- Fecha de entrega: 20/04/2026.

## Objetivo:
Este ejercicio simula un escenario real de desarrollo backend:
- Existe un contrato predefinido (Swagger),
- Se trabaja con un modelo de datos concreto,
- Se deben resolver problemas reales: Filtros, Paginación, Relaciones.
  
## Contenidos evaluados:
- Correcta implementación de endpoints,
- Respeto del contrato API,
- Manejo de paginación,
- Modelado de datos,
- Claridad del código,
- Organización del repositorio.
  
## Integrantes:
- Carla Sabrina, Kim, cskim@fi.uba.ar, 115704;
- Florencia, Avila, flavila@gmail.com, 114386;
- John, Lima, jlima@fi.uba.ar, 115622;
- Kevin Ezequiel, La Rocca, klarocca@fi.uba.ar, 115834;
- Luis, Pérez, lperezj@fi.uba.ar, 115066;
- Neithan, Larez, nlarez@fi.uba.ar, 114904;
- Nicolás Agustín, West, nwest@fi.uba.ar, 115416.

## ¿Por qué decidimos ordenar las carpetas de esta forma?
- En la carpeta app/, estarán todas las implementaciones de los enpoints pedidos (partidos, resultados, usuarios, predicciones, ranking, paginación) ordenados de tal forma en que respeten una arquitectura en capas (más información en docs/arquitectura.md). También por pedido del proyecto, se implementaran como buenas prácticas el manejo de errores y las validaciones de datos.

  > **app/**  
  > Carpeta principal del código de la aplicación. Contiene la inicialización, configuración y los módulos de cada funcionalidad.
  >
  > **usuarios/**  
  > Módulo de usuarios. Contiene routes, service y model para manejar la lógica de usuarios.
  >
  > **partidos/**  
  > Módulo de partidos. Similar a users, con rutas, lógica de negocio y modelos.
  >
  > **prediccion/**   
  > Módulo de predicciones. Igual estructura, para manejar la lógica de predicciones.
  >
  > **ranking/**  
  > Módulo de ranking. Contiene rutas y servicios.
  >
  > **utils/**  
  > Funciones auxiliares compartidas por varios módulos: paginación, validaciones y manejo de errores.

- En la carpeta docs/, se guardarán los archivos que explican y desarrollan todo el proyecto y se explicaran los contenidos y decisiones tomadas durante la implementación de la misma. 

- app.py será el script principal para arrancar la aplicación. 

## Instrucciones de ejecución

### 1. Clonar el repositorio

```bash
git clone <repo_url>
cd <repo>
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=fixture

PORT=5000
DEBUG=True
```

### 5. Crear base de datos

```bash
python -m database.init_db
```

### 6. Ejecutar la aplicación

```bash
python app/app.py
```

La API estará disponible en:

```text
http://localhost:5000
```

## Ejemplos de uso
Como ejemplo de uso tomaremos el endpoint /partidos con el método GET. La idea es, inicialmente, levantar nuestro servidor(en nuestro caso lo levantamos con docker, pero puede ser de otra manera). Luego, ejecutamos python app.py y nos vamos a postman. Dentro de postman, hacemos nuestra conexión con la base de datos, y en donde pone endpoint ponemos http://nuestropuerto/partido, y el método GET. Luego, tocamos "SEND" y nos devolverá, si hicimos las cosas bien, una resputas 200 OK, que fue por que nuestra petición resultó exitosa.

## Hipótesis evaluadas

* Se asume que los IDs son autoincrementales y únicos.
* Se considera que un partido puede no tener resultado al momento de su creación.
* Se asume que un usuario puede realizar **una única predicción por partido**.
* Se asume que las predicciones solo son válidas si el partido aún no tiene resultado cargado.
* Se considera que el cálculo de ranking se realiza dinámicamente a partir de los resultados y predicciones (no se persiste).
* Se asume que la paginación se implementa mediante `_limit` y `_offset`.
* Se asume que los errores siguen el formato definido en el contrato Swagger.
* Se considera que los nombres de equipos son strings sin normalización adicional.

