CREATE OR REPLACE FUNCTION count_total_movies()
RETURNS int
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN COUNT(*) FROM peliculas;
END
$$;

SELECT count_total_movies();