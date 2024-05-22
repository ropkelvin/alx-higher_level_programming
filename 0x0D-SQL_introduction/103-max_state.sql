-- SQL script to find the maximum temperature for each state
-- Select the state and maximum temperature value from the temperatures table
SELECT state, MAX(value) AS max_temp
FROM temperatures
-- Group the results by state to get the maximum temperature for each state
GROUP BY state
-- Order the results by state name in ascending order
ORDER BY state;
