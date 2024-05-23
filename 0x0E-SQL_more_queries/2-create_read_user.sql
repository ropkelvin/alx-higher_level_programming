-- This script creates the MySQL server user user_0d_2 and the database hbtn_0d_2

-- Use the CREATE DATABASE command to create a new database
-- The IF NOT EXISTS option ensures that the script does not fail if the database already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Use the CREATE USER command to create a new user
-- The IF NOT EXISTS option ensures that the script does not fail if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Use the GRANT command to give SELECT privilege to the new user on the new database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Use the FLUSH PRIVILEGES command to reload the grant tables in the mysql database
-- This makes the changes take effect immediately
FLUSH PRIVILEGES;
