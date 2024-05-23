-- script that printts the full description of first_table
-- database name will be passed as an argument 
USE hbtn_0c_0;

SELECT COLUMN_NAME, DATA_TYPE. CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table'