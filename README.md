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
> Módulo de ranking. Contiene rutas, modelo y servicios.
>
> **utils/**  
> Funciones auxiliares compartidas por varios módulos: paginación, validaciones y manejo de errores.

- En la carpeta docs/, se guardarán los archivos que explican y desarrollan todo el proyecto y se explicaran los contenidos y decisiones tomadas durante la implementación de la misma. 

- app.py será el script principal para arrancar la aplicación. 

## Instrucciones de ejecución:
TODO.

## Ejemplos de uso:
TODO.

## Hipótesis evaluadas
TODO.
