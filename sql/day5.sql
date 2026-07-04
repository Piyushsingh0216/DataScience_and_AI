-- Show all students
SELECT * FROM Students;

-- Students with CGPA above 8
SELECT * FROM Students
WHERE cgpa > 8;

-- Top 5 highest CGPA
SELECT * FROM Students
ORDER BY cgpa DESC
LIMIT 5;

-- Department-wise average CGPA
SELECT department,
AVG(cgpa) AS avg_cgpa
FROM Students
GROUP BY department;

-- Cities with more than 2 students
SELECT city,
COUNT(*) AS total_students
FROM Students
GROUP BY city
HAVING COUNT(*) > 2;

-- Highest CGPA
SELECT MAX(cgpa) FROM Students;

-- Lowest CGPA
SELECT MIN(cgpa) FROM Students;