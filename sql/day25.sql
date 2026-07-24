-- =========================================================
-- 1. DATABASE & SCHEMA SETUP
-- =========================================================
CREATE DATABASE interview_practice;
\c interview_practice;

-- Create Tables
CREATE TABLE departments (dept_id INT PRIMARY KEY, dept_name VARCHAR(50));
CREATE TABLE employees (emp_id INT PRIMARY KEY, emp_name VARCHAR(50), salary NUMERIC, dept_id INT);
CREATE TABLE classes (class_id INT PRIMARY KEY, class_name VARCHAR(50));
CREATE TABLE students (student_id INT PRIMARY KEY, student_name VARCHAR(50), marks INT, class_id INT);
CREATE TABLE monthly_sales (sale_month INT PRIMARY KEY, amount NUMERIC);
CREATE TABLE categories (category_id INT PRIMARY KEY, category_name VARCHAR(50));
CREATE TABLE products (product_id INT PRIMARY KEY, product_name VARCHAR(50), sales_amount NUMERIC, category_id INT);
CREATE TABLE user_logs (id INT PRIMARY KEY, name VARCHAR(50), email VARCHAR(50));

-- Insert Dummy Data
INSERT INTO departments VALUES (1, 'Engineering'), (2, 'Sales'), (3, 'HR');
INSERT INTO employees VALUES 
    (1, 'Alice', 90000, 1), (2, 'Bob', 115000, 1), (3, 'Charlie', 85000, 2), 
    (4, 'Diana', 120000, 2), (5, 'Eve', 70000, 3), (6, 'Frank', 95000, 1), 
    (7, 'Grace', 130000, 1), (8, 'Hank', 110000, 2);

INSERT INTO classes VALUES (101, 'Math 101'), (102, 'Science 101');
INSERT INTO students VALUES 
    (1, 'Ivy', 85, 101), (2, 'Jack', 92, 101), (3, 'Karen', 92, 101), 
    (4, 'Leo', 78, 102), (5, 'Mia', 88, 102), (6, 'Noah', 95, 102);

INSERT INTO monthly_sales VALUES 
    (1, 1000), (2, 1500), (3, 1200), (4, 2000), (5, 2500), (6, 2100);

INSERT INTO categories VALUES (1, 'Electronics'), (2, 'Furniture');
INSERT INTO products VALUES 
    (1, 'Laptop', 50000, 1), (2, 'Phone', 30000, 1), (3, 'Tablet', 25000, 1), 
    (4, 'Chair', 5000, 2), (5, 'Desk', 12000, 2), (6, 'Sofa', 45000, 2);

-- Insert duplicates into user_logs
INSERT INTO user_logs VALUES 
    (1, 'Tom', 'tom@example.com'), (2, 'Jerry', 'jerry@example.com'), 
    (3, 'Tom', 'tom@example.com'), (4, 'Spike', 'spike@example.com'), 
    (5, 'Jerry', 'jerry@example.com');


-- =========================================================
-- 2. SQL QUERIES (INTERVIEW PRACTICE)
-- =========================================================

-- Q1: Top 5 highest-paid employees (Using DENSE_RANK & CTE)
WITH RankedEmployees AS (
    SELECT 
        emp_name, 
        salary, 
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employees
)
SELECT * 
FROM RankedEmployees 
WHERE salary_rank <= 5;


-- Q2: Rank students by marks within each class (Using RANK, PARTITION BY & JOIN)
SELECT 
    s.student_name, 
    c.class_name, 
    s.marks, 
    RANK() OVER (PARTITION BY s.class_id ORDER BY s.marks DESC) AS class_rank
FROM students s
JOIN classes c ON s.class_id = c.class_id;


-- Q3: Running total of monthly sales (Using SUM OVER ORDER BY)
SELECT 
    sale_month, 
    amount, 
    SUM(amount) OVER (ORDER BY sale_month) AS running_total
FROM monthly_sales;


-- Q4: Moving average of sales (Using OVER ROWS BETWEEN)
-- Calculates the average of the current month and the previous 2 months
SELECT 
    sale_month, 
    amount, 
    ROUND(AVG(amount) OVER (
        ORDER BY sale_month 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg
FROM monthly_sales;


-- Q5: Employees earning above department average (Using CTE, OVER PARTITION BY & CASE)
WITH DeptStats AS (
    SELECT 
        e.emp_name, 
        e.salary, 
        d.dept_name, 
        AVG(e.salary) OVER (PARTITION BY e.dept_id) AS dept_avg
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
)
SELECT 
    emp_name, 
    dept_name, 
    salary, 
    ROUND(dept_avg, 2) AS dept_avg,
    CASE 
        WHEN salary > dept_avg THEN 'Above Average'
        ELSE 'Below or Equal' 
    END AS status
FROM DeptStats
WHERE salary > dept_avg;


-- Q6: Products with sales above category average (Using JOIN & Window Function in CTE)
WITH CategoryStats AS (
    SELECT 
        p.product_name, 
        p.sales_amount, 
        c.category_name, 
        AVG(p.sales_amount) OVER (PARTITION BY p.category_id) AS cat_avg_sales
    FROM products p
    JOIN categories c ON p.category_id = c.category_id
)
SELECT * 
FROM CategoryStats 
WHERE sales_amount > cat_avg_sales;


-- Q7: Identify duplicate records using window functions (Using ROW_NUMBER)
-- If rn > 1, the record is a duplicate based on the email column.
WITH DuplicateCheck AS (
    SELECT 
        id, 
        name, 
        email, 
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM user_logs
)
SELECT 
    id, 
    name, 
    email, 
    'Duplicate Record' as note
FROM DuplicateCheck 
WHERE rn > 1;