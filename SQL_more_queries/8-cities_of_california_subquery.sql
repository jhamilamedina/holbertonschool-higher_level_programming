-- Enumere todas las ciudades de California que se pueden encontrar en la base de datos hbtn_0d_usa.
-- Los Registros deben ordenarse de manera ascendente(ASC) por cities.id.

SELECT * FROM cities
WHERE state_id = (
	SELECT id 
	FROM cities 
	WHERE name = 'California'
)
ORDER BY id ASC;
