-- Select the 'score' and 'name' from the 'second_table' where 'name' is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
-- Order the result by 'score' in descending order
ORDER BY score DESC;
