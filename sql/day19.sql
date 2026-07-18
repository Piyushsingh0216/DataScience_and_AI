-- ==========================================
-- 0. SETUP: Create Schema and Insert Data
-- ==========================================
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);

INSERT INTO students (id, name, department, marks) VALUES
(1, 'Alice', 'CS', 85),
(2, 'Bob', 'CS', 95),
(3, 'Charlie', 'CS', 70),
(4, 'David', 'IT', 88),
(5, 'Eve', 'IT', 92),
(6, 'Frank', 'IT', 65),
(7, 'Grace', 'Mech', 75),
(8, 'Heidi', 'Mech', 80),
(9, 'Ivan', 'Mech', 80), 
(9, 'Ivan', 'Mech', 80); -- Intentional duplicate record for Question 6


-- ==========================================
-- 1. Top scorer in every department
-- ==========================================
-- We use a CTE (Common Table Expression) with the RANK() window function 
-- to rank students within their own department partition.
WITH RankedStudents AS (
    SELECT id, name, department, marks,
           RANK() OVER (PARTITION BY department ORDER BY marks DESC) as dept_rank
    FROM students
)
SELECT department, name, marks
FROM RankedStudents
WHERE dept_rank = 1;


-- ==========================================
-- 2. Students below department average
-- ==========================================
-- Using the AVG() window function allows us to compare a student's 
-- individual marks directly against their department's average without a JOIN.
WITH DeptStats AS (
    SELECT id, name, department, marks,
           AVG(marks) OVER (PARTITION BY department) as dept_avg
    FROM students
)
SELECT name, department, marks, ROUND(dept_avg, 2) as dept_average
FROM DeptStats
WHERE marks < dept_avg;


-- ==========================================
-- 3. Rank students by marks
-- ==========================================
-- DENSE_RANK() ensures that if two students tie for 3rd, the next student is 4th.
-- RANK() would make the next student 5th.
SELECT id, name, department, marks,
       DENSE_RANK() OVER (ORDER BY marks DESC) as overall_rank
FROM students;


-- ==========================================
-- 4. Running total using Window Functions
-- ==========================================
-- Ordering by ID to create a sequential cumulative sum of the marks.
SELECT id, name, marks,
       SUM(marks) OVER (ORDER BY id) as running_total_marks
FROM students;


-- ==========================================
-- 5. Categorize students into grades using CASE
-- ==========================================
-- Standard IF-THEN logic in SQL via the CASE expression.
SELECT id, name, marks,
       CASE
           WHEN marks >= 90 THEN 'A'
           WHEN marks >= 80 THEN 'B'
           WHEN marks >= 70 THEN 'C'
           ELSE 'F'
       END as grade
FROM students;


-- ==========================================
-- 6. Find duplicate records
-- ==========================================
-- Grouping by all identical columns and filtering for groups having more than 1 entry.
SELECT id, name, department, marks, COUNT(*) as duplicate_count
FROM students
GROUP BY id, name, department, marks
HAVING COUNT(*) > 1;


-- ==========================================
-- 7. Department-wise average marks
-- ==========================================
-- Standard aggregation using GROUP BY.
SELECT department, ROUND(AVG(marks), 2) as avg_marks
FROM students
GROUP BY department
ORDER BY avg_marks DESC;