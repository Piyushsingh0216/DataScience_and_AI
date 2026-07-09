-- 1. Students scoring above their own department average
-- Uses a correlated subquery to compare each student to their specific department's average.
SELECT Student_ID, Department, CGPA
FROM students s1
WHERE CGPA > (
    SELECT AVG(CGPA)
    FROM students s2
    WHERE s1.Department = s2.Department
);

-- 2. Departments with the highest average CGPA
-- Groups by department, calculates the average, sorts it in descending order, and pulls the top result.
SELECT Department, AVG(CGPA) as Avg_CGPA
FROM students
GROUP BY Department
ORDER BY Avg_CGPA DESC
LIMIT 1;

-- 3. Students with the second-highest CGPA
-- Uses the DENSE_RANK() window function to ensure that if multiple students tie for 1st, 
-- the next highest score is accurately captured as 2nd.
WITH RankedStudents AS (
    SELECT 
        Student_ID, 
        Department, 
        CGPA,
        DENSE_RANK() OVER (ORDER BY CGPA DESC) as rank
    FROM students
)
SELECT Student_ID, Department, CGPA
FROM RankedStudents
WHERE rank = 2;

-- 4. Students whose CGPA is greater than ALL students in a specific department (e.g., 'Business')
-- The outer query checks if a student's CGPA is higher than the absolute maximum CGPA in the target department.
SELECT Student_ID, Department, CGPA
FROM students
WHERE CGPA > ALL (
    SELECT CGPA
    FROM students
    WHERE Department = 'Business'
) AND Department != 'Business';

-- 5. Practice query using ANY 
-- Finds students in other departments who have a higher CGPA than AT LEAST ONE student in 'Computer Science'.
SELECT Student_ID, Department, CGPA
FROM students
WHERE CGPA > ANY (
    SELECT CGPA
    FROM students
    WHERE Department = 'Computer Science'
) AND Department != 'Computer Science';