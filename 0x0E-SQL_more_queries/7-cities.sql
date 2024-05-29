-- script that creates database hbtn_0d_usa and table cities drin
-- cities description:
-- id INT unique, auto generated, can't be null and is a primary key
-- state_id INT, can't be null and must be a foreign key that references to id of the states table
-- name varchar(256) can't be null

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

--create table
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);