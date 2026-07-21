-- ==========================================
-- PART 1: CREATE DATABASE SCHEMA & INSERT DATA
-- ==========================================

-- 1. Employees Table (For Q1, Q2, Q3)
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10,2)
);

INSERT INTO employees (employee_id, first_name, department_id, salary) VALUES
(1, 'Alice', 101, 80000),
(2, 'Bob', 101, 95000),
(3, 'Charlie', 102, 60000),
(4, 'David', 102, 75000),
(5, 'Eve', 103, 110000),
(6, 'Frank', 103, 50000),
(7, 'Grace', 103, 105000),
(8, 'Heidi', 101, 90000),
(9, 'Ivan', 102, 70000),
(10, 'Judy', 103, 120000);

-- 2. Daily Revenue Table (For Q4)
CREATE TABLE daily_revenue (
    sales_date DATE,
    daily_sales DECIMAL(10,2)
);

INSERT INTO daily_revenue (sales_date, daily_sales) VALUES
('2023-10-01', 1500),
('2023-10-02', 2000),
('2023-10-03', 1800),
('2023-10-04', 2200),
('2023-10-05', 2500);

-- 3. Orders Table (For Q5, Q6, Q7)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    order_date DATE,
    sales_amount DECIMAL(10,2)
);

INSERT INTO orders (order_id, product_id, customer_id, order_date, sales_amount) VALUES
(1, 201, 301, '2023-01-15', 100),
(2, 202, 301, '2023-02-10', 150),
(3, 201, 302, '2023-01-20', 200),
(4, 203, 303, '2023-01-25', 300),
(5, 202, 304, '2023-02-15', 250),
(6, 201, 301, '2023-03-05', 120),
(7, 202, 302, '2023-03-12', 180),
(8, 201, 305, '2023-01-30', 90),
(9, 201, 306, '2023-02-05', 110),
(10, 201, 307, '2023-03-20', 130);


-- ==========================================
-- PART 2: EXECUTE PRACTICE QUERIES
-- ==========================================

-- 1. Fifth highest salary
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM employees
) ranked_salaries
WHERE rank = 5
LIMIT 1;

-- 2. Employees earning more than the company average
SELECT employee_id, first_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees
);

-- 3. Department-wise top 2 salaries
SELECT department_id, employee_id, salary
FROM (
    SELECT department_id, 
           employee_id, 
           salary,
           DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank
    FROM employees
) ranked_dept_salaries
WHERE rank <= 2;

-- 4. Running average using Window Functions
SELECT sales_date, 
       daily_sales,
       AVG(daily_sales) OVER (
           ORDER BY sales_date 
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_average
FROM daily_revenue;

-- 5. Monthly sales growth
WITH monthly_totals AS (
    SELECT DATE_TRUNC('month', order_date) AS sales_month,
           SUM(sales_amount) AS total_sales
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT sales_month,
       total_sales,
       LAG(total_sales) OVER (ORDER BY sales_month) AS previous_month_sales,
       ROUND(
           ((total_sales - LAG(total_sales) OVER (ORDER BY sales_month)) 
           / LAG(total_sales) OVER (ORDER BY sales_month)) * 100, 2
       ) AS growth_percentage
FROM monthly_totals;

-- 6. Products ordered by fewer than five customers
SELECT product_id
FROM orders
GROUP BY product_id
HAVING COUNT(DISTINCT customer_id) < 5;

-- 7. Customers who purchased every month
SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT DATE_TRUNC('month', order_date)) = (
    SELECT COUNT(DISTINCT DATE_TRUNC('month', order_date)) 
    FROM orders
);