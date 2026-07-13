-- ==========================================
-- 0. SETUP: MOCK DATASET
-- ==========================================
CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(50),
    department VARCHAR(50),
    cgpa DECIMAL(3,2)
);

INSERT INTO students (student_id, student_name, department, cgpa) VALUES
(1, 'Alice', 'Computer Science', 9.50),
(2, 'Bob', 'Mechanical', 8.20),
(3, 'Charlie', 'Computer Science', 8.90),
(4, 'Diana', 'Electrical', 9.10),
(5, 'Eve', 'Mechanical', 9.30),
(6, 'Frank', 'Civil', 7.80),
(7, 'Grace', 'Computer Science', 9.80),
(8, 'Hank', 'Electrical', 8.50),
(9, 'Ivy', 'Civil', 8.80),
(10, 'Jack', 'Mechanical', 7.90);

-- ==========================================
-- 1. Rank students within each department
-- ==========================================
-- Uses PARTITION BY to reset the ranking for each new department.
SELECT 
    student_name, 
    department, 
    cgpa,
    RANK() OVER(PARTITION BY department ORDER BY cgpa DESC) as dept_rank
FROM students;

-- ==========================================
-- 2. Retrieve the top 5 students overall
-- ==========================================
-- Sorts the entire table by CGPA and limits the output to the top 5.
SELECT 
    student_name, 
    department, 
    cgpa
FROM students
ORDER BY cgpa DESC
LIMIT 5; 

-- ==========================================
-- 3. Find the highest CGPA student in each department
-- ==========================================
-- Uses a Common Table Expression (CTE) to temporarily rank students, 
-- then filters for only the students who ranked #1 in their department.
WITH RankedStudents AS (
    SELECT 
        student_name, 
        department, 
        cgpa,
        ROW_NUMBER() OVER(PARTITION BY department ORDER BY cgpa DESC) as rn
    FROM students
)
SELECT 
    department, 
    student_name as top_student, 
    cgpa
FROM RankedStudents
WHERE rn = 1;

-- ==========================================
-- 4. Display each student's rank alongside their department
-- ==========================================
-- Displays both how they stack up globally AND within their specific major.
SELECT 
    student_name,
    department,
    cgpa,
    RANK() OVER(ORDER BY cgpa DESC) as overall_rank,
    RANK() OVER(PARTITION BY department ORDER BY cgpa DESC) as department_rank
FROM students
ORDER BY department, department_rank;