-- ==============================================================================
-- SQL JOINS AND AGGREGATION QUERIES
-- Assumes two tables: 
-- 1. Students (roll_number, name, cgpa, city, dept_id)
-- 2. Departments (dept_id, department_name)
-- ==============================================================================

-- 1. INNER JOIN
-- Returns only the students who are actively assigned to a valid department.
SELECT s.name, s.cgpa, d.department_name
FROM Students s
INNER JOIN Departments d 
    ON s.dept_id = d.dept_id;

-- 2. LEFT JOIN
-- Returns ALL students. If a student has no department assigned, 
-- the department_name column will show as NULL.
SELECT s.name, s.cgpa, d.department_name
FROM Students s
LEFT JOIN Departments d 
    ON s.dept_id = d.dept_id;

-- 3. RIGHT JOIN
-- Returns ALL departments, including those with zero enrolled students. 
-- If a department is empty, the student columns will show as NULL.
SELECT s.name, s.cgpa, d.department_name
FROM Students s
RIGHT JOIN Departments d 
    ON s.dept_id = d.dept_id;

-- 4. CROSS JOIN
-- Creates a Cartesian product, pairing every single student with every 
-- single department (rarely used for standard matching, good for combinations).
SELECT s.name, d.department_name
FROM Students s
CROSS JOIN Departments d;

-- 5. UNION
-- Combines students with a CGPA >= 9.0 and students from Delhi into one list.
-- Removes any duplicate records (e.g., if a 9.0 student is ALSO from Delhi).
SELECT name 
FROM Students 
WHERE cgpa >= 9.0
UNION
SELECT name 
FROM Students 
WHERE city = 'Delhi';

-- 6. UNION ALL
-- Combines the same two lists as above, but KEEPS duplicates. 
-- A 9.0 student from Delhi will appear twice in these results.
SELECT name 
FROM Students 
WHERE cgpa >= 9.0
UNION ALL
SELECT name 
FROM Students 
WHERE city = 'Delhi';

-- 7. DEPARTMENT-WISE AVERAGE CGPA
-- Calculates the mean CGPA for each department using GROUP BY and the AVG() function.
SELECT d.department_name, AVG(s.cgpa) AS average_cgpa
FROM Students s
INNER JOIN Departments d 
    ON s.dept_id = d.dept_id
GROUP BY d.department_name;

-- 8. STUDENTS WITHOUT DEPARTMENTS
-- Filters the table to find students where the foreign key (dept_id) is missing/NULL.
SELECT roll_number, name, cgpa
FROM Students
WHERE dept_id IS NULL;