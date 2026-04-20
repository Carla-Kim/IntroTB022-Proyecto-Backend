-- Active: 1776466306213@@127.0.0.1@3306@proyecto_db

CREATE DATABASE IF NOT EXISTS fixture;
USE fixture;

CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
SELECT * FROM usuarios

CREATE TABLE IF NOT EXISTS partidos(
    id_partido INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(50) NOT NULL,
    equipo_visitante VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    fase VARCHAR(50) NOT NULL CHECK (fase IN ('grupos','dieciseisavos','octavos','cuartos','semis','final')),
    goles_local INT CHECK (goles_local >= 0 OR goles_local IS NULL),
    goles_visitante INT CHECK (goles_visitante >= 0 OR goles_visitante IS NULL),
    CHECK (equipo_local <> equipo_visitante),
    CHECK ((goles_local IS NULL) = (goles_visitante IS NULL))
);

CREATE TABLE IF NOT EXISTS predicciones(
    id_usuario INT NOT NULL,
    id_partido INT NOT NULL,
    goles_local INT NOT NULL CHECK (goles_local >= 0),
    goles_visitante INT NOT NULL CHECK (goles_visitante >= 0),
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

INSERT INTO partidos (equipo_local, equipo_visitante, fecha, fase, goles_local, goles_visitante) VALUES
('Argentina',  'Francia',      '2026-06-15', 'grupos', NULL, NULL),
('Brasil',     'Alemania',     '2026-06-16', 'grupos', 3, 2),
('España',     'Portugal',     '2026-06-17', 'grupos', 0, 1),
('Argentina',  'Brasil',       '2026-07-04', 'cuartos', NULL, NULL),
('Francia',    'Alemania',     '2026-07-05', 'cuartos', 0, 0);

INSERT INTO predicciones (id_usuario, id_partido, goles_local, goles_visitante) VALUES
(1, 1, 3, 0), /*Sin resultados*/
(2, 1, 2, 0), /*Sin resultados*/
(3, 2, 2, 1), /*1 puntos resultado correcto*/
(4, 3, 1, 1), /*0 puntos resultado incorrecto*/
(5, 3, 0, 1), /*3 puntos resultado exacto*/
(6, 4, 2, 0), /*Sin resultados*/
(7, 5, 1, 1); /*1 puntos resultado correcto*/
