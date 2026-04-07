SELECT titulo, MAX(precio_renta)
FROM peliculas
GROUP BY titulo;

SELECT SUM(precio_renta)
FROM peliculas;

SELECT clasificacion, COUNT(*)
FROM peliculas
GROUP BY clasificacion;

SELECT AVG(precio_renta)
FROM peliculas;

SELECT clasificacion, AVG(precio_renta) AS precio_promedio
FROM peliculas
GROUP BY clasificacion
ORDER BY precio_promedio DESC;













