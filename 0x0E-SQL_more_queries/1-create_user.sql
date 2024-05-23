-- This script creates the MySQL server user user_0d_1 with all privileges

-- Use the CREATE USER command to create a new user
-- The IF NOT EXISTS option ensures that the script does not fail if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Use the GRANT command to give all privileges to the new user
-- The *.* means all databases and all tables
-- The WITH GRANT OPTION allows the user to grant or remove other users' privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Use the FLUSH PRIVILEGES command to reload the grant tables in the mysql database
-- This makes the changes take effect immediately
FLUSH PRIVILEGES;
