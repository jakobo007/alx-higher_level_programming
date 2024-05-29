-- script that creates database hbtn_0d_2 and user 'user_0d_2
-- user_0d_2 should have only SELECT priviledge
-- user_0d_2 password should be user_0d_2_pwd
-- if the database already exists the script shouldn't fail
-- if the user  already exists the script shouldn't fail

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

--check if the user exists
SELECT COUNT(*) INTO @count FROM mysql.user WHERE user = 'user_0d_d' AND host = 'localhost'

-- create the user if it doesn't exist
