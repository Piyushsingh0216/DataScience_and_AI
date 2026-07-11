-- ==========================================
-- 0. Mock Data Setup
-- ==========================================
CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    CGPA DECIMAL(3,2)
);

INSERT INTO Students (StudentID, Name, Department, CGPA) VALUES
(1, 'Alice', 'Computer Science', 9.5),
(2, 'Bob', 'Computer Science', 9.5),   -- Tie with Alice
(3, 'Charlie', 'Computer Science', 9.2),
(4, 'Diana', 'Computer Science', 8.8),
(5, 'Eve', 'Mathematics', 9.8),
(6, 'Frank', 'Mathematics', 9.1),
(7, 'Grace', 'Mathematics', 9.1),    -- Tie with Frank
(8, 'Hank', 'Mathematics', 8.5),
(9, 'Ivy', 'Physics', 9.0),
(10, 'Jack', 'Physics', 8.4);

-- ==========================================
-- 1. Rank students by CGPA (Overall)
-- ==========================================
-- This ranks everyone across the whole table. 
SELECT 
    Name, 
    Department, 
    CGPA, 
    RANK() OVER (ORDER BY CGPA DESC) AS overall_rank
FROM Students;

-- ==========================================
-- 2. Find the top 3 students in each department
-- ==========================================
-- Window functions cannot be directly used in a WHERE clause, 
-- so we wrap the logic in a Common Table Expression (CTE).
WITH RankedStudents AS (
    SELECT 
        Name, 
        Department, 
        CGPA, 
        DENSE_RANK() OVER (PARTITION BY Department ORDER BY CGPA DESC) AS dept_rank
    FROM Students
)
SELECT * FROM RankedStudents 
WHERE dept_rank <= 3;

-- ==========================================
-- 3. Assign row numbers within each department
-- ==========================================
-- ROW_NUMBER simply increments by 1 for each row in the partition, 
-- completely ignoring ties (Alice and Bob will get 1 and 2 arbitrarily).
SELECT 
    Name, 
    Department, 
    CGPA, 
    ROW_NUMBER() OVER (PARTITION BY Department ORDER BY CGPA DESC) AS row_num
FROM Students;

-- ==========================================
-- 4. Compare RANK() and DENSE_RANK()
-- ==========================================
-- Observe Alice/Bob and Frank/Grace to see how ties are handled differently.
SELECT 
    Name, 
    Department, 
    CGPA, 
    RANK() OVER (ORDER BY CGPA DESC) AS regular_rank,
    DENSE_RANK() OVER (ORDER BY CGPA DESC) AS dense_rank
FROM Students
ORDER BY CGPA DESC;