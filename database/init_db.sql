CREATE DATABASE IF NOT EXISTS fixture;
USE fixture;

CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS partidos(
    id_partido INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(50) NOT NULL,
    equipo_visitante VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    fase VARCHAR(50) NOT NULL CHECK (fase IN ('grupos','dieciseisavos','octavos','cuartos','semis','final')),
    resultados VARCHAR(50) 
);


CREATE TABLE IF NOT EXISTS predicciones(
    id_usuario INT NOT NULL,
    id_partido INT NOT NULL,
    local INT NOT NULL CHECK (local >= 0),
    visitante INT NOT NULL CHECK (visitante >= 0),
    PRIMARY KEY (id_usuario, id_partido),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_partido) REFERENCES partidos(id_partido) ON DELETE CASCADE
);


INSERT INTO usuarios (nombre, email) VALUES
('Florencia Avila', 'flavila@fi.uba.ar'),
('Carla Kim', 'cskim@fi.uba.ar'),
('John Lima', 'jlima@fi.uba.ar'),
('Kevin La Rocca', 'klarocca@fi.uba.ar'),
('Luis Perez', 'lperezj@fi.uba.ar'),
('Neithan Larez', 'nlarez@fi.uba.ar'),
('Nicolas West', 'nwest@fi.uba.ar');

INSERT INTO partidos (equipo_local, equipo_visitante, fecha, fase) VALUES
('Argentina',  'Francia',      '2026-06-15', 'grupos'),
('Brasil',     'Alemania',     '2026-06-16', 'grupos'),
('España',     'Portugal',     '2026-06-17', 'grupos'),
('Argentina',  'Brasil',       '2026-07-04', 'cuartos'),
('Francia',    'Alemania',     '2026-07-05', 'cuartos');


INSERT INTO predicciones (id_usuario, id_partido, local, visitante) VALUES
(1, 1, 3, 0), /*3 puntos resultado exacto */
(2, 1, 2, 0), /*1 punto resultado correcto*/
(3, 2, 0, 1), /*0 puntos resultado incorrecto*/
(4, 3, 1, 1), /*3 puntos resultado exacto*/
(5, 3, 0, 0), /*1 punto resultado correcto*/
(6, 4, 2, 0), /*1 punto resultado correcto*/
(7, 5, 0, 2); /*1 puntos resultado correcto*/

