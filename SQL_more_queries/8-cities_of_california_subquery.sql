-- Enumere todas las ciudades de California que se pueden encontrar en la base de datos hbtn_0d_usa.
-- Los Registros deben ordenarse de manera ascendente(ASC) por cities.id.

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
