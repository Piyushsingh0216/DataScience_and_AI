ALTER TABLE Students
ADD department VARCHAR(50);

ALTER TABLE Students
ADD cgpa DECIMAL(3,2);

UPDATE Students
SET department='CSE-AI',
    city='Lucknow',
    cgpa=8.90
WHERE id=1;

UPDATE Students
SET department='CSE',
    city='Delhi',
    cgpa=7.80
WHERE id=2;

UPDATE Students
SET department='IT',
    city='Gorakhpur',
    cgpa=9.20
WHERE id=3;

SELECT DISTINCT department FROM Students;

SELECT department, COUNT(*) AS total_students
FROM Students
GROUP BY department;

SELECT department, AVG(cgpa) AS average_cgpa
FROM Students
GROUP BY department;

SELECT department, COUNT(*)
FROM Students
GROUP BY department
HAVING COUNT(*) > 5;

SELECT city, COUNT(*) AS total_students
FROM Students
GROUP BY city;