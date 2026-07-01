-- Create Database
CREATE DATABASE College;

-- Use Database
USE College;

-- Create Table
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

-- Insert Data
INSERT INTO Students VALUES
(1,'Piyush',21,'Lucknow'),
(2,'Rahul',20,'Delhi'),
(3,'Aman',22,'Gorakhpur');

-- Display Data
SELECT * FROM Students;
