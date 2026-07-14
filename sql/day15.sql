-- ==========================================
-- 0. Setup Mock Database
-- ==========================================
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    CGPA DECIMAL(3, 2)
);

INSERT INTO Students (Student_ID, Name, Department, CGPA) VALUES
(1, 'Alice', 'Computer Science', 9.2),
(2, 'Bob', 'Computer Science', 8.5),
(3, 'Charlie', 'Computer Science', 7.8),
(4, 'David', 'Computer Science', 9.5),
(5, 'Eva', 'Electrical', 8.1),
(6, 'Frank', 'Electrical', 7.4),
(7, 'Grace', 'Electrical', 8.9),
(8, 'Hank', 'Mechanical', 6.5),
(9, 'Ivy', 'Mechanical', 7.2),
(10, 'Jack', 'Mechanical', 8.0);

-- ==========================================
-- 1. Find the top 3 students in each department
-- ==========================================
-- We use a Common Table Expression (CTE) and the DENSE_RANK() window function.
WITH RankedStudents AS (
    SELECT 
        Name, 
        Department, 
        CGPA, 
        DENSE_RANK() OVER(PARTITION BY Department ORDER BY CGPA DESC) as Dept_Rank
    FROM Students
)
SELECT * FROM RankedStudents 
WHERE Dept_Rank <= 3;

-- ==========================================
-- 2. Find departments with an average CGPA above a threshold (e.g., 8.0)
-- ==========================================
-- The HAVING clause is used instead of WHERE because we are filtering on an aggregated value.
SELECT 
    Department, 
    AVG(CGPA) as Average_CGPA 
FROM Students 
GROUP BY Department 
HAVING AVG(CGPA) > 8.0;

-- ==========================================
-- 3. Retrieve students whose CGPA is above the overall average
-- ==========================================
-- We use a subquery to first calculate the overall average, then filter against it.
SELECT 
    Name, 
    Department, 
    CGPA 
FROM Students 
WHERE CGPA > (
    SELECT AVG(CGPA) FROM Students
);

-- ==========================================
-- 4. Display each student's department rank
-- ==========================================
-- The RANK() window function assigns a rank within each specific department partition.
SELECT 
    Name, 
    Department, 
    CGPA, 
    RANK() OVER(PARTITION BY Department ORDER BY CGPA DESC) as Rank_In_Dept
FROM Students;

-- ==========================================
-- 5. Count students in each department
-- ==========================================
-- Standard GROUP BY with the COUNT() aggregate function.
SELECT 
    Department, 
    COUNT(*) as Total_Students 
FROM Students 
GROUP BY Department;