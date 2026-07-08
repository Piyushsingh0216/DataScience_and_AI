-- =======================================================
-- 1. Students with above-average CGPA
-- =======================================================
SELECT * FROM students 
WHERE cgpa > (SELECT AVG(cgpa) FROM students);


-- =======================================================
-- 2. Students in the department with the highest average CGPA
-- =======================================================
SELECT * FROM students 
WHERE department = (
    SELECT department 
    FROM students 
    GROUP BY department 
    ORDER BY AVG(cgpa) DESC 
    LIMIT 1
);


-- =======================================================
-- 3. Departments having more than 5 students
-- =======================================================
SELECT department, COUNT(*) as student_count 
FROM students 
GROUP BY department 
HAVING COUNT(*) > 5;


-- =======================================================
-- 4. Students whose CGPA equals the maximum CGPA
-- =======================================================
SELECT * FROM students 
WHERE cgpa = (SELECT MAX(cgpa) FROM students);
