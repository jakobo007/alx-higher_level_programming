-- script that lists all the priviledges of MySQL users user_0d_1 and user_0d_2 on the server in localhost
-- Connect to the MySQL server
-- Make sure to replace 'root' and 'your_root_password' with your actual MySQL root username and password

-- Display privileges for user_0d_1
SELECT 'user_0d_1' AS 'User', 
       t1.Host AS 'Host', 
       t1.Db AS 'Database',
       t2.Privilege_type AS 'Privilege'
FROM (SELECT Host, Db 
	      FROM mysql.db 
	      WHERE User='user_0d_1'
	      UNION ALL
	      SELECT Host, '%' AS Db 
	      FROM mysql.user 
	      WHERE User='user_0d_1') AS t1
JOIN (SELECT Host, Db, Privilege_type 
	      FROM information_schema.schema_privileges 
	      WHERE Grantee LIKE '\'user_0d_1\'@\'%\') AS t2
ON t1.Host = t2.Host AND (t1.Db = t2.Db OR t2.Db = '%%');

-- Display global privileges for user_0d_1
SELECT 'user_0d_1' AS 'User', 
       Host AS 'Host', 
       'Global' AS 'Scope',
       Privilege_type AS 'Privilege'
FROM information_schema.user_privileges 
WHERE Grantee LIKE '\'user_0d_1\'@\'%\';

-- Display privileges for user_0d_2
SELECT 'user_0d_2' AS 'User', 
       t1.Host AS 'Host', 
       t1.Db AS 'Database',
       t2.Privilege_type AS 'Privilege'
FROM (SELECT Host, Db 
	      FROM mysql.db 
	      WHERE User='user_0d_2'
	      UNION ALL
	      SELECT Host, '%' AS Db 
	      FROM mysql.user 
	      WHERE User='user_0d_2') AS t1
JOIN (SELECT Host, Db, Privilege_type 
	      FROM information_schema.schema_privileges 
	      WHERE Grantee LIKE '\'user_0d_2\'@\'%\') AS t2
ON t1.Host = t2.Host AND (t1.Db = t2.Db OR t2.Db = '%%');

-- Display global privileges for user_0d_2
SELECT 'user_0d_2' AS 'User', 
       Host AS 'Host', 
       'Global' AS 'Scope',
       Privilege_type AS 'Privilege'
FROM information_schema.user_privileges 
WHERE Grantee LIKE '\'user_0d_2\'@\'%\';

