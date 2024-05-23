-- scrpit that lists number of records with the same score in the table
-- resuls should display the score, the number of records for this score with the label number
USE hbtn_0c_0;

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;