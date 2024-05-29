-- script that lists all the cities that can be found in database hbtn_0d_usa
-- The states table contains only one record where name = California but id can be different
-- results must be sorted in ascending order by cities.id

USE hbtn_0d_usa;

-- Retrive the state_id of california from the states table
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of california
SELECT * FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;