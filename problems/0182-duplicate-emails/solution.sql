# Write your MySQL query statement below
# SELECT DISTINCT email, count(*) from Person
SELECT email from Person group by email having count(*) > 1

