-- script that displays the number of record with id=89 in first_table
-- database name will be passed as argument
USE hbtn_0c_0;

SELECT COUNT(*) AS counter
FROM first_table
WHERE id = 89;
