-- ==========================================
-- 0. Setup: Create Mock Dataset
-- ==========================================
CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    cgpa DECIMAL(3,2)
);

INSERT INTO students VALUES 
(1, 'Alice', 'Computer Science', 9.2),
(2, 'Bob', 'Computer Science', 8.5),
(3, 'Charlie', 'Computer Science', 7.8),
(4, 'Diana', 'Computer Science', 8.9),
(5, 'Eve', 'Mechanical', 9.5),
(6, 'Frank', 'Mechanical', 7.1),
(7, 'Grace', 'Mechanical', 8.8),
(8, 'Heidi', 'Electrical', 9.1),
(9, 'Ivan', 'Electrical', 8.2),
(10, 'Judy', 'Electrical', 7.5);


-- ==========================================
-- 1. Top 3 students in each department
-- ==========================================
-- Using DENSE_RANK() allows us to partition the data by department 
-- and rank them independently by CGPA.
SELECT student_id, name, department, cgpa
FROM (
    SELECT student_id, name, department, cgpa,
           DENSE_RANK() OVER(PARTITION BY department ORDER BY cgpa DESC) as rnk
    FROM students
) ranked_students
WHERE rnk <= 3;


-- ==========================================
-- 2. Students above department average 
-- (Using a Correlated Subquery)
-- ==========================================
-- The subquery calculates the average for the specific department 
-- of the current row being evaluated in the outer query.
SELECT name, department, cgpa
FROM students s1
WHERE cgpa > (
    SELECT AVG(cgpa) 
    FROM students s2 
    WHERE s1.department = s2.department
);


-- ==========================================
-- 3. Rank students by CGPA
-- ==========================================
-- RANK() skips numbers if there's a tie (e.g., 1, 2, 2, 4). 
-- If you want sequential numbers (1, 2, 2, 3), use DENSE_RANK().
SELECT student_id, name, department, cgpa,
       RANK() OVER(ORDER BY cgpa DESC) as university_rank
FROM students;


-- ==========================================
-- 4. Count students by department
-- ==========================================
SELECT department, COUNT(student_id) as total_students
FROM students
GROUP BY department
ORDER BY total_students DESC;


-- ==========================================
-- 5. Categorize students into performance bands
-- ==========================================
SELECT name, department, cgpa,
    CASE 
        WHEN cgpa >= 9.0 THEN 'Outstanding'
        WHEN cgpa >= 8.0 THEN 'Excellent'
        WHEN cgpa >= 7.0 THEN 'Good'
        ELSE 'Needs Improvement'
    END as performance_band
FROM students
ORDER BY cgpa DESC;


-- ==========================================
-- 6. Rewrite Query #2 using a CTE instead 
-- of a nested subquery
-- ==========================================
-- CTEs (Common Table Expressions) make complex queries easier to read 
-- by isolating the aggregation logic before the main SELECT statement.
WITH DepartmentAverages AS (
    SELECT department, AVG(cgpa) as avg_cgpa
    FROM students
    GROUP BY department
)
SELECT s.name, s.department, s.cgpa, ROUND(da.avg_cgpa, 2) as dept_avg
FROM students s
JOIN DepartmentAverages da 
  ON s.department = da.department
WHERE s.cgpa > da.avg_cgpa;