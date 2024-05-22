-- Create the table 'second_table' if it doesn't already exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,              -- 'id' column, type INT
    name VARCHAR(256),   -- 'name' column, type VARCHAR(256)
    score INT            -- 'score' column, type INT
);

-- Insert the specified records into the 'second_table'
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),   -- Record 1
(2, 'Alex', 3),    -- Record 2
(3, 'Bob', 14),    -- Record 3
(4, 'George', 8);  -- Record 4
