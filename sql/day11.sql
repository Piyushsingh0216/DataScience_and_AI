-- =========================================================================
-- 1. Create a view showing students with CGPA > 8
-- =========================================================================
-- This creates a virtual table that updates automatically as underlying data changes.
CREATE VIEW high_achievers AS
SELECT 
    student_id, 
    name, 
    department, 
    cgpa
FROM students
WHERE cgpa > 8.0;

-- To see the results of the view:
-- SELECT * FROM high_achievers;


-- =========================================================================
-- 2. Use a CTE to calculate department-wise average CGPA
-- =========================================================================
-- CTEs (Common Table Expressions) make complex queries easier to read.
WITH DepartmentAverages AS (
    SELECT 
        department, 
        AVG(cgpa) AS avg_cgpa
    FROM students
    GROUP BY department
)
-- Selecting from the CTE to display the results
SELECT * FROM DepartmentAverages;


-- =========================================================================
-- 3. Display students above their department average using a CTE
-- =========================================================================
-- Reusing the logic from above, we join the CTE back to the main table.
WITH DepartmentAverages AS (
    SELECT 
        department, 
        AVG(cgpa) AS avg_cgpa
    FROM students
    GROUP BY department
)
SELECT 
    s.name, 
    s.department, 
    s.cgpa, 
    d.avg_cgpa
FROM students s
JOIN DepartmentAverages d ON s.department = d.department
WHERE s.cgpa > d.avg_cgpa;


-- =========================================================================
-- 4. Rewrite an earlier subquery using a CTE
-- =========================================================================
-- SCENARIO: Let's assume an earlier subquery found students with the highest overall CGPA.
-- The old subquery way would look like this:
-- SELECT name, cgpa FROM students WHERE cgpa = (SELECT MAX(cgpa) FROM students);

-- REWRITTEN as a CTE:
WITH MaxCGPA AS (
    SELECT MAX(cgpa) AS highest_cgpa 
    FROM students
)
SELECT 
    s.name, 
    s.cgpa
FROM students s
JOIN MaxCGPA m ON s.cgpa = m.highest_cgpa;