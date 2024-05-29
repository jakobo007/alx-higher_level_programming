-- script that creates database hbtn_0d_usa and the table states inside it
-- states description: id INt unique, auto generated, can't be null and is a primary key
-- name varchar(256)

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);