-- This script creates the table force_name on your MySQL server

-- Use the CREATE TABLE command to create a new table
-- The IF NOT EXISTS option ensures that the script does not fail if the table already exists
CREATE TABLE IF NOT EXISTS force_name (
    -- id is of type INT
    id INT,
    -- name is of type VARCHAR(256) and can't be null
    name VARCHAR(256) NOT NULL
);
