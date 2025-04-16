from app import db
from datetime import datetime

# User-defined types
class Address(db.TypeDecorator):
    impl = db.String
    
    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return f"{value['street']}, {value['city']}, {value['state']}, {value['zip']}"
    
    def process_result_value(self, value, dialect):
        if value is None:
            return None
        street, city, state, zip_code = value.split(', ')
        return {'street': street, 'city': city, 'state': state, 'zip': zip_code}

# Base Person class (inheritance)
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date)
    address = db.Column(Address)
    type = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }

# Student class (inherits from Person)
class Student(Person):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    enrollment_date = db.Column(db.Date, default=datetime.utcnow)
    major = db.Column(db.String(100))
    
    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

# Faculty class (inherits from Person)
class Faculty(Person):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    faculty_id = db.Column(db.String(20), unique=True, nullable=False)
    hire_date = db.Column(db.Date, default=datetime.utcnow)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    specializations = db.Column(db.ARRAY(db.String))
    
    __mapper_args__ = {
        'polymorphic_identity': 'faculty',
    }

# Department class
class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    building = db.Column(db.String(100))
    budget = db.Column(db.Numeric(10, 2))
    faculty = db.relationship('Faculty', backref='department')
    courses = db.relationship('Course', backref='department')

# Course class
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    credits = db.Column(db.Integer, default=3)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    prerequisites = db.Column(db.ARRAY(db.String))
    
# Enrollment class (many-to-many relationship)
class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.String(2))
    
    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))
