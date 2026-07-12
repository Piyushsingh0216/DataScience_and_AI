-- ==========================================
-- 0. SETUP: Create table and insert dummy data
-- ==========================================
CREATE TABLE students (
    student_id VARCHAR(10),
    name VARCHAR(50),
    department VARCHAR(50),
    cgpa DECIMAL(3, 2)
);

INSERT INTO students (student_id, name, department, cgpa) VALUES
('S01', 'Alice', 'Computer Science', 3.8),
('S02', 'Bob', 'Computer Science', 4.0),
('S03', 'Charlie', 'Computer Science', 4.0), -- Tie for CS
('S04', 'David', 'Mechanical', 3.5),
('S05', 'Eva', 'Mechanical', 3.8),
('S06', 'Frank', 'Mechanical', 3.9),
('S07', 'Grace', 'Civil', 3.2),
('S08', 'Hank', 'Civil', 3.9),
('S09', 'Ivy', 'Civil', 3.9);                 -- Tie for Civil

-- ==========================================
-- 1. Rank students by CGPA within each department
-- ==========================================
SELECT 
    student_id,
    name,
    department,
    cgpa,
    RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) AS dept_rank
FROM 
    students;

-- ==========================================
-- 2. Find the second-highest CGPA in each department
-- ==========================================
WITH RankedStudents AS (
    SELECT 
        student_id,
        name,
        department,
        cgpa,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) AS cgpa_rank
    FROM 
        students
)
SELECT 
    student_id,
    name,
    department,
    cgpa
FROM 
    RankedStudents
WHERE 
    cgpa_rank = 2;

-- ==========================================
-- 3. Display the top 3 students department-wise
-- ==========================================
WITH TopStudents AS (
    SELECT 
        student_id,
        name,
        department,
        cgpa,
        RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) AS cgpa_rank
    FROM 
        students
)
SELECT 
    student_id,
    name,
    department,
    cgpa,
    cgpa_rank
FROM 
    TopStudents
WHERE 
    cgpa_rank <= 3;

-- ==========================================
-- 4. Compare RANK() and DENSE_RANK() on tied values
-- ==========================================
SELECT 
    name,
    department,
    cgpa,
    RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) AS regular_rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY cgpa DESC) AS dense_rank
FROM 
    students;
    