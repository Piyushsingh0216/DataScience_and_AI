-- =======================================================
-- 1. SETUP: Create Tables & Insert Mock Data
-- =======================================================
CREATE TABLE employees (employee_id INT, employee_name VARCHAR(50), department_id INT, salary INT);
INSERT INTO employees VALUES (1, 'Alice', 1, 90000), (2, 'Bob', 1, 85000), (3, 'Charlie', 2, 95000), (4, 'Diana', 2, 95000), (5, 'Eve', 1, 70000);

CREATE TABLE students (student_id INT, student_name VARCHAR(50), department_id INT, marks INT);
INSERT INTO students VALUES (1, 'Tom', 101, 88), (2, 'Jerry', 101, 95), (3, 'Spike', 102, 75), (4, 'Tyke', 102, 99);

CREATE TABLE daily_sales (order_date DATE, sales_amount INT);
INSERT INTO daily_sales VALUES ('2023-01-01', 100), ('2023-01-02', 150), ('2023-01-03', 200);

CREATE TABLE users (id INT, email VARCHAR(100));
INSERT INTO users VALUES (1, 'test@test.com'), (2, 'hello@world.com'), (3, 'test@test.com');

CREATE TABLE customers (customer_id INT, customer_name VARCHAR(50));
CREATE TABLE orders (order_id INT, customer_id INT);
INSERT INTO customers VALUES (1, 'John'), (2, 'Sarah'), (3, 'Mike');
INSERT INTO orders VALUES (1001, 1), (1002, 2);

CREATE TABLE sales (order_id INT, order_date DATE, sales_amount INT);
INSERT INTO sales VALUES (1, '2023-10-15', 500), (2, '2023-10-20', 300), (3, '2023-11-05', 400);

-- =======================================================
-- 2. EXECUTE QUERIES
-- =======================================================

SELECT '--- 1. Second Highest Salary ---' AS Query_Title;
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);


SELECT '--- 2. Department-wise Highest Marks ---' AS Query_Title;
WITH RankedStudents AS (
    SELECT 
        student_id, student_name, department_id, marks,
        ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY marks DESC) as rn
    FROM students
)
SELECT student_id, student_name, department_id, marks
FROM RankedStudents
WHERE rn = 1;


SELECT '--- 3. Running Total Using Window Functions ---' AS Query_Title;
SELECT 
    order_date, 
    sales_amount,
    SUM(sales_amount) OVER (ORDER BY order_date) AS running_total
FROM daily_sales;


SELECT '--- 4. Rank Employees by Salary ---' AS Query_Title;
SELECT 
    employee_id, employee_name, salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;


SELECT '--- 5. Duplicate Records ---' AS Query_Title;
WITH DuplicateCheck AS (
    SELECT 
        id, email, 
        ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) as rn
    FROM users
)
SELECT id, email 
FROM DuplicateCheck 
WHERE rn > 1;


SELECT '--- 6. Customers With No Orders ---' AS Query_Title;
SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


SELECT '--- 7. Monthly Sales Summary ---' AS Query_Title;
-- Note: EXTRACT works in PostgreSQL/MySQL. 
-- (If you paste this into SQLite, change EXTRACT(YEAR FROM order_date) to STRFTIME('%Y', order_date) and MONTH to '%m')
SELECT 
    EXTRACT(YEAR FROM order_date) AS sales_year,
    EXTRACT(MONTH FROM order_date) AS sales_month,
    COUNT(order_id) AS total_orders,
    SUM(sales_amount) AS total_revenue
FROM sales
GROUP BY 
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY 
    sales_year DESC, 
    sales_month DESC;