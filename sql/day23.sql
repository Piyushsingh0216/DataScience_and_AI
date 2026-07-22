-- ==========================================
-- A. CREATE DATABASE AND USE IT
-- ==========================================
CREATE DATABASE CompanyDB;
USE CompanyDB;

-- ==========================================
-- B. CREATE TABLES
-- ==========================================
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY, 
    dept_name VARCHAR(50)
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY, 
    emp_name VARCHAR(50), 
    dept_id INT, 
    salary DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY, 
    product_name VARCHAR(50), 
    total_sales DECIMAL(10,2)
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY, 
    customer_name VARCHAR(50)
);

CREATE TABLE Purchases (
    purchase_id INT PRIMARY KEY, 
    customer_id INT, 
    purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY, 
    order_date DATE, 
    amount DECIMAL(10,2)
);

CREATE TABLE Users (
    user_id INT PRIMARY KEY, 
    email VARCHAR(100)
);

-- ==========================================
-- C. INSERT SAMPLE DATA
-- ==========================================
INSERT INTO Departments (dept_id, dept_name) VALUES 
(1, 'Engineering'), (2, 'Sales'), (3, 'HR');

INSERT INTO Employees (emp_id, emp_name, dept_id, salary) VALUES 
(1, 'Alice', 1, 90000), (2, 'Bob', 1, 120000), (3, 'Charlie', 1, 120000),
(4, 'Diana', 2, 85000), (5, 'Evan', 2, 95000), (6, 'Fiona', 3, 70000);

INSERT INTO Products (product_id, product_name, total_sales) VALUES 
(1, 'Laptop', 500000), (2, 'Phone', 750000), (3, 'Tablet', 250000), (4, 'Monitor', 250000);

INSERT INTO Customers (customer_id, customer_name) VALUES 
(1, 'George'), (2, 'Hannah'), (3, 'Ian');

INSERT INTO Purchases (purchase_id, customer_id, purchase_date) VALUES 
(1, 1, CURRENT_DATE - INTERVAL '5 days'),
(2, 2, CURRENT_DATE - INTERVAL '40 days'); -- Older than 1 month

INSERT INTO Orders (order_id, order_date, amount) VALUES 
(1, '2023-10-15', 30000), (2, '2023-10-20', 25000), 
(3, '2023-11-05', 15000), (4, '2023-11-12', 10000);

INSERT INTO Users (user_id, email) VALUES 
(1, 'alice@example.com'), (2, 'bob@example.com'), (3, 'alice@example.com');

-- ==========================================
-- D. RUN ANALYTICAL QUERIES
-- ==========================================

-- 1. Employees with the highest salary in each department
WITH RankedSalaries AS (
    SELECT 
        e.emp_id, 
        e.emp_name, 
        d.dept_name, 
        e.salary,
        RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) as salary_rank
    FROM Employees e
    JOIN Departments d ON e.dept_id = d.dept_id
)
SELECT emp_name, dept_name, salary
FROM RankedSalaries
WHERE salary_rank = 1;


-- 2. Second highest salary without using LIMIT
SELECT MAX(salary) AS SecondHighestSalary
FROM Employees
WHERE salary < (
    SELECT MAX(salary) 
    FROM Employees
);


-- 3. Department-wise running totals
SELECT 
    e.emp_name, 
    d.dept_name, 
    e.salary,
    SUM(e.salary) OVER (PARTITION BY e.dept_id ORDER BY e.emp_id) AS dept_running_total
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;


-- 4. Rank products by sales
SELECT 
    product_name, 
    total_sales,
    DENSE_RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
FROM Products;


-- 5. Customers with no purchases in the last month
SELECT c.customer_id, c.customer_name
FROM Customers c
LEFT JOIN Purchases p 
    ON c.customer_id = p.customer_id 
    AND p.purchase_date >= CURRENT_DATE - INTERVAL '1 month'
WHERE p.purchase_id IS NULL;


-- 6. Monthly revenue summary
SELECT 
    EXTRACT(MONTH FROM order_date) AS order_month,
    EXTRACT(YEAR FROM order_date) AS order_year,
    SUM(amount) AS monthly_revenue,
    CASE 
        WHEN SUM(amount) >= 50000 THEN 'High Target Met'
        WHEN SUM(amount) >= 20000 THEN 'Moderate Performance'
        ELSE 'Needs Improvement'
    END AS performance_status
FROM Orders
GROUP BY 
    EXTRACT(YEAR FROM order_date), 
    EXTRACT(MONTH FROM order_date)
ORDER BY 
    order_year DESC, 
    order_month DESC;


-- 7. Duplicate email detection
SELECT 
    email, 
    COUNT(email) AS occurrence_count
FROM Users
GROUP BY email
HAVING COUNT(email) > 1;