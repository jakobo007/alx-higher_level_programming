-- script that creates a second_table in hbtn_0c_0
-- description: id INT, name VARCHAR(256), score INT
-- if table already exists script shouldn't fail
-- insert values/ records after to the table
USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS second_table (
    id = INT,
    name = VARCHAR(256),
    score = INT
);

-- insert rows

INSERT INTO second_table(id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    score = VALUES(score)