from app import mongo_db
from datetime import datetime

# MongoDB collections
students_collection = mongo_db.students
courses_collection = mongo_db.courses
departments_collection = mongo_db.departments

def insert_sample_data():
    # Clear existing data
    students_collection.delete_many({})
    courses_collection.delete_many({})
    departments_collection.delete_many({})
    
    # Insert departments
    departments = [
        {
            "name": "Computer Science",
            "building": "Tech Building",
            "budget": 500000.00,
            "faculty": [
                {
                    "id": "F20001",
                    "name": "Robert Johnson",
                    "email": "robert.johnson@example.com",
                    "date_of_birth": datetime(1980, 3, 10),
                    "address": {
                        "street": "789 Oak St",
                        "city": "Cambridge",
                        "state": "MA",
                        "zip": "02139"
                    },
                    "hire_date": datetime(2015, 8, 15),
                    "specializations": ["Artificial Intelligence", "Machine Learning"]
                }
            ]
        },
        {
            "name": "Mathematics",
            "building": "Science Hall",
            "budget": 350000.00,
            "faculty": [
                {
                    "id": "F20002",
                    "name": "Mary Williams",
                    "email": "mary.williams@example.com",
                    "date_of_birth": datetime(1975, 11, 28),
                    "address": {
                        "street": "101 Pine St",
                        "city": "Boston",
                        "state": "MA",
                        "zip": "02118"
                    },
                    "hire_date": datetime(2010, 1, 10),
                    "specializations": ["Number Theory", "Algebra"]
                }
            ]
        },
        {
            "name": "Physics",
            "building": "Science Hall",
            "budget": 400000.00,
            "faculty": []
        }
    ]
    
    departments_collection.insert_many(departments)
    
    # Insert courses with embedded department info
    courses = [
        {
            "code": "CS101",
            "title": "Introduction to Programming",
            "description": "Basic programming concepts using Python",
            "credits": 3,
            "department": {
                "name": "Computer Science",
                "building": "Tech Building"
            },
            "prerequisites": [],
            "students_enrolled": []
        },
        {
            "code": "CS201",
            "title": "Data Structures",
            "description": "Advanced data structures and algorithms",
            "credits": 4,
            "department": {
                "name": "Computer Science",
                "building": "Tech Building"
            },
            "prerequisites": ["CS101"],
            "students_enrolled": []
        },
        {
            "code": "MATH101",
            "title": "Calculus I",
            "description": "Introduction to differential calculus",
            "credits": 4,
            "department": {
                "name": "Mathematics",
                "building": "Science Hall"
            },
            "prerequisites": [],
            "students_enrolled": []
        },
        {
            "code": "PHYS101",
            "title": "Physics I",
            "description": "Mechanics and thermodynamics",
            "credits": 4,
            "department": {
                "name": "Physics",
                "building": "Science Hall"
            },
            "prerequisites": ["MATH101"],
            "students_enrolled": []
        }
    ]
    
    courses_collection.insert_many(courses)
    
    # Insert students with embedded enrollment info
    students = [
        {
            "student_id": "S10001",
            "name": "John Smith",
            "email": "john.smith@example.com",
            "date_of_birth": datetime(1995, 5, 15),
            "address": {
                "street": "123 Main St",
                "city": "Boston",
                "state": "MA",
                "zip": "02115"
            },
            "enrollment_date": datetime(2020, 9, 1),
            "major": "Computer Science",
            "enrollments": [
                {
                    "course_code": "CS101",
                    "course_title": "Introduction to Programming",
                    "enrollment_date": datetime(2020, 9, 5),
                    "grade": "A"
                },
                {
                    "course_code": "CS201",
                    "course_title": "Data Structures",
                    "enrollment_date": datetime(2021, 1, 20),
                    "grade": "B+"
                }
            ]
        },
        {
            "student_id": "S10002",
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "date_of_birth": datetime(1997, 8, 22),
            "address": {
                "street": "456 Park Ave",
                "city": "Boston",
                "state": "MA",
                "zip": "02116"
            },
            "enrollment_date": datetime(2021, 1, 15),
            "major": "Mathematics",
            "enrollments": [
                {
                    "course_code": "MATH101",
                    "course_title": "Calculus I",
                    "enrollment_date": datetime(2021, 1, 20),
                    "grade": "A-"
                },
                {
                    "course_code": "PHYS101",
                    "course_title": "Physics I",
                    "enrollment_date": datetime(2021, 1, 20),
                    "grade": "B"
                }
            ]
        }
    ]
    
    students_collection.insert_many(students)
    
    # Update courses with enrolled students
    courses_collection.update_one(
        {"code": "CS101"},
        {"$push": {"students_enrolled": {"student_id": "S10001", "name": "John Smith", "grade": "A"}}}
    )
    
    courses_collection.update_one(
        {"code": "CS201"},
        {"$push": {"students_enrolled": {"student_id": "S10001", "name": "John Smith", "grade": "B+"}}}
    )
    
    courses_collection.update_one(
        {"code": "MATH101"},
        {"$push": {"students_enrolled": {"student_id": "S10002", "name": "Jane Doe", "grade": "A-"}}}
    )
    
    courses_collection.update_one(
        {"code": "PHYS101"},
        {"$push": {"students_enrolled": {"student_id": "S10002", "name": "Jane Doe", "grade": "B"}}}
    )
