-- This SQL script selects the top 3 cities with the highest average temperature in July and August

-- Select the city and average temperature columns
SELECT city, AVG(value) as avg_temp
FROM temperatures  -- From the temperatures table
WHERE month IN (7, 8)  -- Only consider the months of July and August
GROUP BY city  -- Group the results by city
ORDER BY avg_temp DESC  -- Order the results by average temperature in descending order
LIMIT 3;  -- Limit the results to the top 3
