-- Script that creates database hbtn_0d_2 and user 'user_0d_2'
-- user_0d_2 should have only SELECT privilege
-- user_0d_2 password should be user_0d_2_pwd
-- if the database already exists the script shouldn't fail
-- if the user already exists the script shouldn't fail

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user exists
SELECT COUNT(*) INTO @count FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';

-- Create the user if it does not exist
SET @create_user = IF(@count = 0, 'CREATE USER \'user_0d_2\'@\'localhost\' IDENTIFIED BY \'user_0d_2_pwd\';', 'SELECT "User already exists";');

PREPARE stmt FROM @create_user;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant SELECT privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;

