UPDATE Students
SET city = 'Lucknow'
WHERE id = 1;

DELETE FROM Students
WHERE id = 5;

SELECT COUNT(*) FROM Students;

SELECT AVG(age) FROM Students;

SELECT MAX(age) FROM Students;

SELECT MIN(age) FROM Students;

SELECT SUM(age) FROM Students;