-- Create tables
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL
);

CREATE TABLE StudentsDepartments (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    DepartmentID INT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Insert sample data
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'CSE'),
(2, 'ECE'),
(3, 'IT');

INSERT INTO StudentsDepartments (StudentID, StudentName, DepartmentID) VALUES
(101, 'Piyush', 1),
(102, 'Rahul', 2),
(103, 'Aman', NULL),
(104, 'Sneha', 3),
(105, 'Riya', NULL);

-- 1. Student with Department Name
SELECT
    s.StudentID,
    s.StudentName,
    d.DepartmentName
FROM StudentsDepartments s
LEFT JOIN Departments d ON s.DepartmentID = d.DepartmentID;

-- 2. Students without Department
SELECT
    s.StudentID,
    s.StudentName
FROM StudentsDepartments s
LEFT JOIN Departments d ON s.DepartmentID = d.DepartmentID
WHERE d.DepartmentID IS NULL;

-- 3. All Departments
SELECT
    DepartmentID,
    DepartmentName
FROM Departments;

-- 4. Count Students in each Department
SELECT
    d.DepartmentName,
    COUNT(s.StudentID) AS StudentCount
FROM Departments d
LEFT JOIN StudentsDepartments s ON d.DepartmentID = s.DepartmentID
GROUP BY d.DepartmentID, d.DepartmentName
ORDER BY d.DepartmentName;
