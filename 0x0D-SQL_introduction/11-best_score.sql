-- script that list all records with a score >= 10 in second_table
-- results should display both the score and name (in this order)
-- records should be ordered by score
USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;