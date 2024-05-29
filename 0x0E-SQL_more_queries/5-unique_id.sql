-- script that creates table unique_id
-- description id INT default value 1 and must be unique
-- name VARCHAR(256)
use hbtn_0d_2;

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);