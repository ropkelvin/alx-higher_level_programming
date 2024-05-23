-- This script creates a table named 'unique_id' in your MySQL server

-- The 'IF NOT EXISTS' clause prevents an error from occurring if the table already exists
CREATE TABLE IF NOT EXISTS unique_id (
    -- 'id' column of type INT with a default value of 1 and must be unique
    id INT DEFAULT 1 UNIQUE,
    -- 'name' column of type VARCHAR(256)
    name VARCHAR(256)
);
