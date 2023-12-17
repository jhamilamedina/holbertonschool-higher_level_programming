-- Enumere todos los programas contenidos en hbtn_0d_tvshows que tengan al menos un género vinculado.
-- Importe el volcado de la base de datos de hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
