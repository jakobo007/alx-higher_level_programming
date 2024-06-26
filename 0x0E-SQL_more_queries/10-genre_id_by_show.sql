-- script that lists all the shows contained in hbtn_0d_tvshows that have at least one genre linked
-- each record should display tv_shows.title - tvshows.genre_id
-- results should be sorted in ascending order by tv_shows.title and tv_show_genres.genre.id
USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id