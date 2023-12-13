-- Enumere todas las ciudades contenidas en la base de datos.
-- Cada registro debe mostrar: ciudades.id - ciudades.nombre - estados.nombre en formas ASC.

SELECT cities.id, cities.name AS city, states.name AS state
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
