-- script that updates the score of Bob in second_table
-- database name will be passed as argument
USE hbtn_0c_0;

UPDATE score
SET score = 10
WHERE name = 'Bob';