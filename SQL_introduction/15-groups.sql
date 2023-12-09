-- Enumerar la cantidad de registros con la misma puntuación en la tabla second_table.
SELECT score AS score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
