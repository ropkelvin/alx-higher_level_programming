-- This SQL script creates a table named 'first_table' if it doesn't already exist
CREATE TABLE IF NOT EXISTS first_table (
    -- 'id' column, data type is INT (integer)
    id INT,
    -- 'name' column, data type is VARCHAR(256)
    -- which can hold a string with a maximum length of 256 characters
    name VARCHAR(256)
);
