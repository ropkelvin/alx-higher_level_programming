-- This script calculates the average temperature by city
-- and orders the results in descending order

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
