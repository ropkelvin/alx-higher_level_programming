-- Select the 'score' and the count of records for each 'score' from the 'second_table'
SELECT score, COUNT(*) AS number FROM second_table
-- Group the results by 'score'
GROUP BY score
-- Order the result by the count ('number') in descending order
ORDER BY number DESC;
