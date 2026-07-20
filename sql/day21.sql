-- ==============================================================================
-- PART 1: SCHEMA CREATION (DDL)
-- ==============================================================================
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10, 2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10, 2)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- ==============================================================================
-- PART 2: INSERTING DATA (DML)
-- ==============================================================================
INSERT INTO Departments (dept_id, dept_name) VALUES 
(1, 'Engineering'), (2, 'Sales'), (3, 'HR');

INSERT INTO Employees (emp_id, name, salary, dept_id) VALUES 
(1, 'Alice', 95000, 1),
(2, 'Bob', 120000, 1),
(3, 'Charlie', 85000, 1),
(4, 'Diana', 120000, 2), -- Tie for highest salary overall
(5, 'Evan', 75000, 2),
(6, 'Fiona', 105000, 2), -- 3rd highest overall
(7, 'George', 60000, 3);

INSERT INTO Customers (customer_id, customer_name) VALUES 
(1, 'Acme Corp'), (2, 'Globex'), (3, 'Initech');

INSERT INTO Products (product_id, product_name, price) VALUES 
(101, 'Laptop', 1200.00),
(102, 'Monitor', 300.00),
(103, 'Desk Chair', 250.00),
(104, 'Webcam', 80.00); -- This product will never be ordered

INSERT INTO Orders (order_id, customer_id, order_date, amount) VALUES 
(1001, 1, '2023-01-15', 1500.00),
(1002, 1, '2023-01-20', 300.00),
(1003, 2, '2023-02-10', 1200.00),
(1004, 3, '2023-02-15', 250.00),
(1005, 3, '2023-03-05', 1450.00);

INSERT INTO Order_Items (item_id, order_id, product_id) VALUES 
(1, 1001, 101), (2, 1001, 102),
(3, 1002, 102),
(4, 1003, 101),
(5, 1004, 103),
(6, 1005, 101), (7, 1005, 103);

-- ==============================================================================
-- PART 3: EXECUTING QUERIES ON THE DATA (DQL)
-- ==============================================================================

-- 1. Third highest salary overall
WITH RankedSalaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM Employees
)
SELECT DISTINCT salary 
FROM RankedSalaries 
WHERE rank = 3;
-- Expected Output: 95000.00


-- 2. Employees earning above their department average
SELECT e1.name, e1.salary, d.dept_name
FROM Employees e1
JOIN Departments d ON e1.dept_id = d.dept_id
WHERE e1.salary > (
    SELECT AVG(salary) 
    FROM Employees e2 
    WHERE e1.dept_id = e2.dept_id
);
-- Expected Output: Bob (Engineering), Diana & Fiona (Sales)


-- 3. Dense ranking by department
SELECT 
    d.dept_name,
    e.name, 
    e.salary, 
    DENSE_RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) as dept_rank
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;
-- Expected Output: Ranks employees 1, 2, 3 internally within Eng, Sales, and HR.


-- 4. Monthly sales report (Standard ANSI approach using EXTRACT)
SELECT 
    EXTRACT(YEAR FROM order_date) AS sale_year,
    EXTRACT(MONTH FROM order_date) AS sale_month,
    SUM(amount) AS total_revenue, 
    COUNT(order_id) AS total_orders
FROM Orders
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY sale_year DESC, sale_month DESC;
-- Expected Output: Aggregations for Jan, Feb, and Mar 2023.


-- 5. Running total of sales
SELECT 
    order_id,
    order_date, 
    amount, 
    SUM(amount) OVER (ORDER BY order_date, order_id) AS running_total
FROM Orders;
-- Expected Output: Cumulative sum rolling from 1500 -> 1800 -> 3000 -> 3250 -> 4700.


-- 6. Customers with multiple orders
SELECT 
    c.customer_name, 
    COUNT(o.order_id) AS total_orders
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;
-- Expected Output: Acme Corp (2), Initech (2)


-- 7. Products never ordered
SELECT 
    p.product_id, 
    p.product_name 
FROM Products p
LEFT JOIN Order_Items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;
-- Expected Output: Webcam (104)