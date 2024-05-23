-- script that creates a table first_table in current database
-- description: id INT, name VARCHAR(256)
-- database name will be passed as an argument
use hbtn_0c_0;

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);