-- script that lists all records of the table
-- dont show list rows without a name
-- results should display the score and the name (in this order)
-- records should be listed by ascending order
USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE name IS NOT NULL and name != ''
ORDER BY score DESC;