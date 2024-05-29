-- script that lists all the shows contained in the database hbtn_0d_tvshows
-- each record should display tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in asceinding order by tv_shows.title and tv_show_genres.genre_id
-- if the show doesn't have a genre display NULL
-- you can only use one select statement

USE hbtn_0d_tvshows;

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
