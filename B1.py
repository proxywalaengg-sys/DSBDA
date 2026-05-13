# 1.Create databases and tables, insert small amounts of data, and run simple queries using Impala

-- =====================================================
-- IMPALA PROGRAM
-- Aim: Create database and tables, insert data,
--      and run simple queries using Apache Impala
-- =====================================================

-- Step 1: Create Database
CREATE DATABASE student_db;

-- Step 2: Use Database
USE student_db;

-- Step 3: Create Table
CREATE TABLE student (
    id INT,
    name STRING,
    age INT,
    department STRING
);

-- Step 4: Insert Records
INSERT INTO student VALUES
(1, 'Rahul', 20, 'Computer'),
(2, 'Sneha', 21, 'IT'),
(3, 'Amit', 22, 'ENTC'),
(4, 'Priya', 19, 'Mechanical'),
(5, 'Karan', 23, 'Civil');

-- Step 5: Display All Records
SELECT * FROM student;

-- =====================================================
-- SIMPLE QUERIES
-- =====================================================

-- Query 1: Display only student names
SELECT name FROM student;

-- Query 2: Display students age greater than 20
SELECT * FROM student
WHERE age > 20;

-- Query 3: Display students from IT department
SELECT * FROM student
WHERE department = 'IT';

-- Query 4: Sort records by name
SELECT * FROM student
ORDER BY name;

-- Query 5: Count total number of students
SELECT COUNT(*) FROM student;

-- Query 6: Find maximum age
SELECT MAX(age) FROM student;

-- Query 7: Find minimum age
SELECT MIN(age) FROM student;

-- Query 8: Find average age
SELECT AVG(age) FROM student;

-- Query 9: Display unique departments
SELECT DISTINCT department FROM student;

-- Query 10: Delete a record
DELETE FROM student
WHERE id = 5;

-- Step 6: Display Final Table
SELECT * FROM student;