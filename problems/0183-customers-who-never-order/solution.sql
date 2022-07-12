# Write your MySQL query statement below

SELECT
    C.name as Customers
From 
    Customers as C
LEFT JOIN Orders as O on O.customerId = C.id
WHERE O.customerId is null
