-- ==========================================
-- 0. SETUP: MOCK DATA FOR TESTING
-- ==========================================
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    cgpa DECIMAL(3,2)
);

INSERT INTO students (student_id, name, department, cgpa) VALUES
(1, 'Alice', 'Computer Science', 9.2),
(2, 'Bob', 'Computer Science', 8.5),
(3, 'Charlie', 'Computer Science', 9.5),
(4, 'David', 'Computer Science', 8.8),
(5, 'Eve', 'Mechanical', 7.5),
(6, 'Frank', 'Mechanical', 8.1),
(7, 'Grace', 'Mechanical', 7.9),
(8, 'Heidi', 'Mechanical', 9.0),
(9, 'Ivan', 'Electrical', 8.4),
(10, 'Judy', 'Electrical', 8.4); 
-- (Assuming the Electrical department has < 10 students for query 4 testing)

-- ==========================================
-- 1. TOP 3 STUDENTS BY CGPA IN EVERY DEPARTMENT
-- ==========================================
-- We use a subquery with DENSE_RANK() to avoid gaps if two students have the exact same CGPA.
SELECT name, department, cgpa
FROM (
    SELECT 
        name, 
        department, 
        cgpa,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) as rnk
    FROM students
) ranked_table
WHERE rnk <= 3;

-- ==========================================
-- 2. STUDENTS ABOVE THE OVERALL AVERAGE CGPA
-- ==========================================
-- A standard subquery calculates the global average first, then the outer query filters by it.
SELECT name, department, cgpa
FROM students
WHERE cgpa > (
    SELECT AVG(cgpa) FROM students
);

-- ==========================================
-- 3. EACH STUDENT'S DEPARTMENT RANK
-- ==========================================
-- Standard window function without the need for a WHERE clause or subquery.
SELECT 
    name, 
    department, 
    cgpa,
    RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) as dept_rank
FROM students;

-- ==========================================
-- 4. DEPARTMENTS WITH MORE THAN 10 STUDENTS
-- ==========================================
-- GROUP BY aggregates the departments, and HAVING filters on the aggregated count.
SELECT 
    department, 
    COUNT(student_id) as total_students
FROM students
GROUP BY department
HAVING COUNT(student_id) > 10;

-- ==========================================
-- 5. REWRITE USING BOTH A CTE AND A WINDOW FUNCTION
-- ==========================================
-- Rewriting Query #1 (Top 3 students) using a Common Table Expression (CTE) 
-- instead of a traditional subquery for better readability.

WITH RankedStudents AS (
    SELECT 
        name, 
        department, 
        cgpa,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) as dept_rank
    FROM students
)
SELECT 
    name, 
    department, 
    cgpa, 
    dept_rank
FROM RankedStudents
WHERE dept_rank <= 3;
