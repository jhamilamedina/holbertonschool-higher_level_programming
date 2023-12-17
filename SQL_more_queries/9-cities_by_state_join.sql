-- Enumere todas las ciudades contenidas en la base de datos.
-- Cada registro debe mostrar: ciudades.id - ciudades.nombre - estados.nombre en formas ASC.

SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
