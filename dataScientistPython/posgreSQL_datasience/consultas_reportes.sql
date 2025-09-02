CREATE OR REPLACE FUNCTION movies_stats()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE-- ANTES DE BEGIN, DEBEMOS DECLARAR NUESTRAS VARIABLES
    total_rated_r REAL := 0.0; -- := sirve para asignar valor
    total_larger_than_100 REAL := 0.0; -- REAL permite operar con decimales
    total_published_2006 REAL := 0.0;
    duration_avg REAL := 0.0;
    rental_price_avg REAL := 0.0;
BEGIN
    total_rated_r := count(*) from peliculas WHERE clasificacion = 'R';
    total_larger_than_100 := count(*) FROM peliculas WHERE duracion > 100;
    total_published_2006 := count(*) FROM peliculas WHERE anio_publicacion = 2006;
    duration_avg := avg(duracion) FROM peliculas;
    rental_price_avg := avg(precio_renta) FROM peliculas;
    
    TRUNCATE table peliculas_estadisticas;
    
    INSERT INTO peliculas_estadisticas(tipo_estadistica,total) VALUES 
        ('Peliculas con clasificacion R', total_rated_r),
        ('Peliculas de mas de 100 minutos', total_larger_than_100),
        ('Peliculas publicadas en 2006',total_published_2006),
        ('Promedio de duracion en minutos', duration_avg),
        ('Precio promedio de renta', rental_price_avg);
    
    RETURN NEW;
END
$$;


SELECT movies_stats();