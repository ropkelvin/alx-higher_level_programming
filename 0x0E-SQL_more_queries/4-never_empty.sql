-- This script creates a table named 'id_not_null' in your MySQL server

-- The 'IF NOT EXISTS' clause prevents an error from occurring if the table already exists
CREATE TABLE IF NOT EXISTS id_not_null (
    -- 'id' column of type INT with a default value of 1
    id INT DEFAULT 1,
    -- 'name' column of type VARCHAR(256)
    name VARCHAR(256)
);
