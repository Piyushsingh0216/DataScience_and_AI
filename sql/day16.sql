-- ==========================================
-- 0. Setup: Create Table & Insert Mock Data
-- ==========================================
CREATE TABLE Students (
    Student_ID INT,
    Department VARCHAR(50),
    CGPA DECIMAL(3, 2)
);

INSERT INTO Students (Student_ID, Department, CGPA) VALUES
(1, 'Computer Science', 9.2), (2, 'Computer Science', 8.5), (3, 'Computer Science', 9.8),
(4, 'Mechanical', 7.5), (5, 'Mechanical', 8.1), (6, 'Mechanical', 6.9),
(7, 'Electrical', 8.8), (8, 'Electrical', 9.1), (9, 'Electrical', 8.8),
(10, 'Civil', 7.2), (11, 'Civil', 8.4), (12, 'Civil', 9.0);

-- ==========================================
-- 1. Rank students department-wise by CGPA
-- ==========================================
-- Using DENSE_RANK() ensures no gaps in ranking if two students have the exact same CGPA.
SELECT 
    Student_ID, 
    Department, 
    CGPA,
    DENSE_RANK() OVER(PARTITION BY Department ORDER BY CGPA DESC) AS Dept_Rank
FROM Students;

-- ==========================================
-- 2. Find the top 2 students in each department
-- ==========================================
-- We wrap the ranking function in a Common Table Expression (CTE) so we can filter by the rank.
WITH RankedStudents AS (
    SELECT 
        Student_ID, 
        Department, 
        CGPA,
        DENSE_RANK() OVER(PARTITION BY Department ORDER BY CGPA DESC) AS Dept_Rank
    FROM Students
)
SELECT Student_ID, Department, CGPA, Dept_Rank
FROM RankedStudents
WHERE Dept_Rank <= 2;

-- ==========================================
-- 3. Display departments with above-average overall CGPA
-- ==========================================
-- Compares the department's average against the global average of all students.
SELECT 
    Department, 
    AVG(CGPA) AS Dept_Avg_CGPA
FROM Students
GROUP BY Department
HAVING AVG(CGPA) > (SELECT AVG(CGPA) FROM Students);

-- ==========================================
-- 4A. Find students with CGPA higher than Dept average (Using a CTE)
-- ==========================================
-- Best practice for readability and complex joins.
WITH DeptAverages AS (
    SELECT Department, AVG(CGPA) AS Dept_Avg
    FROM Students
    GROUP BY Department
)
SELECT 
    s.Student_ID, 
    s.Department, 
    s.CGPA, 
    d.Dept_Avg
FROM Students s
JOIN DeptAverages d ON s.Department = d.Department
WHERE s.CGPA > d.Dept_Avg;

-- ==========================================
-- 4B. Find students with CGPA higher than Dept average (Using a Subquery)
-- ==========================================
-- Uses a Correlated Subquery (the subquery runs for every row evaluated in the outer query).
SELECT 
    Student_ID, 
    Department, 
    CGPA
FROM Students s
WHERE CGPA > (
    SELECT AVG(CGPA)
    FROM Students
    WHERE Department = s.Department
);