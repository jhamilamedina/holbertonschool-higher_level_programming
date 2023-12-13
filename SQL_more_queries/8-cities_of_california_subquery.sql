-- Enumere todas las ciudades de California que se pueden encontrar en la base de datos hbtn_0d_usa.
-- Los Registros deben ordenarse de manera ascendente(ASC) por cities.id.

SELECT * FROM cities
WHERE state.id = (
	SELECT ID
	FROM states
	WHERE name = 'California'
)
ORDER BY ID ASC;
