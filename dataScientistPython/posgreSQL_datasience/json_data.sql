CREATE TABLE ordenes (
	ID serial NOT NULL PRIMARY KEY,
	info json NOT NULL
);

INSERT INTO ordenes(info)
VALUES(
	'{"cliente":"David Bocanegra", "items":{"producto":"Biberon", "cantidad":24}}'),
	('{"cliente":"Juan Bocanegra", "items":{"producto":"Carro", "cantidad":3}}');

SELECT 
	info -> 'cliente' AS cliente
FROM ordenes;

-- Esta segunda seccion no da el valor pero no a modo de string, sino como valor
SELECT 
	info ->> 'cliente' AS cliente
FROM ordenes;

SELECT
	info ->> 'cliente' AS cliente 
FROM ordenes
WHERE info -> 'items' ->> 'producto' = 'Biberon'