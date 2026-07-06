-- Create Departments table
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

-- Create Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Create Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- Create Enrollments table (Mapping table for many-to-many relationship)
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Student + Department
SELECT 
    s.student_name, 
    d.dept_name
FROM 
    Students s
JOIN 
    Departments d ON s.dept_id = d.dept_id;

-- Student + Course
SELECT 
    s.student_name, 
    c.course_name
FROM 
    Students s
JOIN 
    Enrollments e ON s.student_id = e.student_id
JOIN 
    Courses c ON e.course_id = c.course_id;

-- Count students in each department
SELECT 
    d.dept_name, 
    COUNT(s.student_id) AS total_students
FROM 
    Departments d
LEFT JOIN 
    Students s ON d.dept_id = s.dept_id
GROUP BY 
    d.dept_id, 
    d.dept_name;

-- Departments with no students
SELECT 
    d.dept_name
FROM 
    Departments d
LEFT JOIN 
    Students s ON d.dept_id = s.dept_id
WHERE 
    s.student_id IS NULL;

-- Students enrolled in multiple courses
SELECT 
    s.student_name, 
    COUNT(e.course_id) AS course_count
FROM 
    Students s
JOIN 
    Enrollments e ON s.student_id = e.student_id
GROUP BY 
    s.student_id, 
    s.student_name
HAVING 
    COUNT(e.course_id) > 1;