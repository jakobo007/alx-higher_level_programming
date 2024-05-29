-- Check if the user 'user_0d_1'@'localhost' already exists
SELECT COUNT(*) INTO @count FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

-- Create the user if it does not exist
SET @create_user = IF(@count = 0, 'CREATE USER \'user_0d_1\'@\'localhost\' IDENTIFIED BY \'user_0d_1_pwd\';', 'SELECT "User already exists";');
PREPARE stmt FROM @create_user;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES
ON *.* 
TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure that all changes take effect
FLUSH PRIVILEGES;

