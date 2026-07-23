-- ====================================================================================
-- INITIALIZATION: Create Database and Schema
-- ====================================================================================
CREATE DATABASE CorporateAnalyticsDB;
USE CorporateAnalyticsDB;

-- Create necessary tables to support the queries
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(12, 2),
    department_id INT,
    manager_id INT
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(12, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);

CREATE TABLE Order_Details (
    order_id INT,
    product_id INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- ====================================================================================
-- 1. Fourth Highest Salary (Using CTE and Window Functions)
-- ====================================================================================
WITH RankedSalaries AS (
    SELECT 
        salary, 
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM Employees
)
SELECT DISTINCT salary AS fourth_highest_salary
FROM RankedSalaries
WHERE salary_rank = 4;

-- ====================================================================================
-- 2. Top 3 Salaries in Each Department (Using CTE and Window Functions)
-- ====================================================================================
WITH DepartmentRankings AS (
    SELECT 
        department_id, 
        employee_id, 
        salary,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
    FROM Employees
)
SELECT 
    department_id, 
    employee_id, 
    salary
FROM DepartmentRankings
WHERE dept_rank <= 3;

-- ====================================================================================
-- 3. Department-wise Running Average (Using Window Functions)
-- ====================================================================================
SELECT 
    department_id, 
    employee_id, 
    salary,
    AVG(salary) OVER (
        PARTITION BY department_id 
        ORDER BY employee_id 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_avg_salary
FROM Employees;

-- ====================================================================================
-- 4. Monthly Revenue Trend (Using Aggregate Functions, Window Functions, and CASE)
-- ====================================================================================
WITH MonthlyRevenue AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS order_month,
        SUM(order_amount) AS total_revenue
    FROM Orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT 
    order_month,
    total_revenue,
    CASE 
        WHEN total_revenue > LAG(total_revenue) OVER (ORDER BY order_month) THEN 'Up'
        WHEN total_revenue < LAG(total_revenue) OVER (ORDER BY order_month) THEN 'Down'
        ELSE 'Flat/No Prior Data'
    END AS revenue_trend
FROM MonthlyRevenue
ORDER BY order_month;

-- ====================================================================================
-- 5. Employees Without Managers (Using Subqueries)
-- ====================================================================================
SELECT 
    employee_id, 
    first_name, 
    last_name
FROM Employees
WHERE manager_id IS NULL 
   OR manager_id NOT IN (SELECT employee_id FROM Employees);

-- ====================================================================================
-- 6. Customers Who Placed More Than Five Orders (Using JOINs and Aggregate Functions)
-- ====================================================================================
SELECT 
    c.customer_id, 
    c.customer_name, 
    COUNT(o.order_id) AS total_orders
FROM Customers c
INNER JOIN Orders o 
    ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, 
    c.customer_name
HAVING COUNT(o.order_id) > 5;

-- ====================================================================================
-- 7. Products Never Sold (Using JOINs and Subqueries)
-- ====================================================================================
SELECT 
    product_id, 
    product_name
FROM Products
WHERE product_id NOT IN (
    SELECT DISTINCT product_id 
    FROM Order_Details 
    WHERE product_id IS NOT NULL
);