-- script that lists all records of the second_table
-- results shoulld display both the score and the name (in this order)
-- record should be displayed by score (top first)
USE hbtn_0c_0;

SELECT score, name
FROM second_table
ORDER BY score DESC;