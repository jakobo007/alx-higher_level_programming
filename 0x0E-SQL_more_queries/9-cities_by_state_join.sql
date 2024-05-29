-- script that lists all cities contained in hbtn_0d_usa
-- ceach record should display cities.id - cities.name- states.name
-- results should be in ascending order by cities.id
-- you can use ONLY one SELECT statement

USE hbtn_0d_usa;

-- list all cities with corresponding state name
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = state_id
ORDER BY cities.id ASC;