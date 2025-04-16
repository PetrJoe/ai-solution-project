-- Drop tables if they exist
DROP TABLE IF EXISTS enrollment;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS department;

-- Create tables with inheritance and complex data types
CREATE TABLE department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    building VARCHAR(100),
    budget DECIMAL(10, 2)
);

CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    address TEXT,
    type VARCHAR(50)
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY REFERENCES person(id),
    student_id VARCHAR(20) UNIQUE NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    major VARCHAR(100)
);

CREATE TABLE faculty (
    id INTEGER PRIMARY KEY REFERENCES person(id),
    faculty_id VARCHAR(20) UNIQUE NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE,
    department_id INTEGER REFERENCES department(id),
    specializations VARCHAR[] -- Array type
);

CREATE TABLE course (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    credits INTEGER DEFAULT 3,
    department_id INTEGER REFERENCES department(id),
    prerequisites VARCHAR[] -- Array type
);

CREATE TABLE enrollment (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES student(id) NOT NULL,
    course_id INTEGER REFERENCES course(id) NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(2)
);

-- Create a trigger to ensure enrollment date is not in the future
CREATE OR REPLACE FUNCTION check_enrollment_date()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.enrollment_date > CURRENT_TIMESTAMP THEN
        RAISE EXCEPTION 'Enrollment date cannot be in the future';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enrollment_date_check
BEFORE INSERT OR UPDATE ON enrollment
FOR EACH ROW EXECUTE FUNCTION check_enrollment_date();

-- Insert sample data
-- Departments
INSERT INTO department (name, building, budget) VALUES 
('Computer Science', 'Tech Building', 500000.00),
('Mathematics', 'Science Hall', 350000.00),
('Physics', 'Science Hall', 400000.00);

-- Persons (base for students and faculty)
INSERT INTO person (name, email, date_of_birth, address, type) VALUES
('John Smith', 'john.smith@example.com', '1995-05-15', '123 Main St, Boston, MA, 02115', 'student'),
('Jane Doe', 'jane.doe@example.com', '1997-08-22', '456 Park Ave, Boston, MA, 02116', 'student'),
('Robert Johnson', 'robert.johnson@example.com', '1980-03-10', '789 Oak St, Cambridge, MA, 02139', 'faculty'),
('Mary Williams', 'mary.williams@example.com', '1975-11-28', '101 Pine St, Boston, MA, 02118', 'faculty');

-- Students
INSERT INTO student (id, student_id, enrollment_date, major) VALUES
(1, 'S10001', '2020-09-01', 'Computer Science'),
(2, 'S10002', '2021-01-15', 'Mathematics');

-- Faculty
INSERT INTO faculty (id, faculty_id, hire_date, department_id, specializations) VALUES
(3, 'F20001', '2015-08-15', 1, ARRAY['Artificial Intelligence', 'Machine Learning']),
(4, 'F20002', '2010-01-10', 2, ARRAY['Number Theory', 'Algebra']);

-- Courses
INSERT INTO course (code, title, description, credits, department_id, prerequisites) VALUES
('CS101', 'Introduction to Programming', 'Basic programming concepts using Python', 3, 1, ARRAY[]::VARCHAR[]),
('CS201', 'Data Structures', 'Advanced data structures and algorithms', 4, 1, ARRAY['CS101']),
('MATH101', 'Calculus I', 'Introduction to differential calculus', 4, 2, ARRAY[]::VARCHAR[]),
('PHYS101', 'Physics I', 'Mechanics and thermodynamics', 4, 3, ARRAY['MATH101']);

-- Enrollments
INSERT INTO enrollment (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2020-09-05', 'A'),
(1, 2, '2021-01-20', 'B+'),
(2, 3, '2021-01-20', 'A-'),
(2, 4, '2021-01-20', 'B');
