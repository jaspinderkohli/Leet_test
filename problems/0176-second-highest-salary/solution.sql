# Write your MySQL query statement below
SELECT ( select DISTINCT salary from Employee 
ORDER BY Salary DESC LIMIT 1 OFFSET 1 ) AS SecondHighestSalary;
