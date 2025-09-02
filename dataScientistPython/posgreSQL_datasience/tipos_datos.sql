CREATE TYPE humor AS ENUM ('tristr', 'normal', 'feliz');

CREATE TABLE persona_prueba(
	nombre text,
	humor_actual humor
);

INSERT INTO persona_prueba VALUES ('david', 'feliz');