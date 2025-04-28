from flask import render_template, jsonify, request
from app import app, db, mongo_db
from app.models.postgresql_models import Student, Faculty, Department, Course, Enrollment
from app.models.mongodb_models import insert_sample_data
import psycopg2
import json
from bson import json_util

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

@app.route('/api/postgresql/students')
def postgresql_students():
    students = Student.query.all()
    result = []
    for student in students:
        result.append({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'student_id': student.student_id,
            'major': student.major
        })
    return jsonify(result)

@app.route('/api/postgresql/complex-query')
def postgresql_complex_query():
    # Example of a complex query with multiple joins
    # This query gets all students, their enrolled courses, and the departments offering those courses
    # conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
    conn = psycopg2.connect(app.config['POSTGRESQL_DSN'])
    cursor = conn.cursor()
    
    query = """
    SELECT s.name as student_name, s.student_id, c.title as course_title, 
           c.code as course_code, d.name as department_name, e.grade
    FROM student s
    INNER JOIN enrollment e ON s.id = e.student_id
    LEFT OUTER JOIN course c ON e.course_id = c.id
    FULL OUTER JOIN department d ON c.department_id = d.id
    ORDER BY s.name, c.title
    """
    
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    conn.close()
    
    return jsonify(result)

@app.route('/api/mongodb/students')
def mongodb_students():
    students = list(mongo_db.students.find({}, {'_id': 0}))
    return json.loads(json_util.dumps(students))

@app.route('/api/mongodb/complex-query')
def mongodb_complex_query():
    # Example of a complex MongoDB aggregation query
    # This query gets all courses with their enrolled students and department info
    pipeline = [
        {
            '$lookup': {
                'from': 'departments',
                'localField': 'department.name',
                'foreignField': 'name',
                'as': 'department_info'
            }
        },
        {
            '$unwind': {
                'path': '$department_info',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$project': {
                '_id': 0,
                'code': 1,
                'title': 1,
                'credits': 1,
                'department_name': '$department.name',
                'department_building': '$department.building',
                'students_enrolled': 1,
                'faculty': '$department_info.faculty'
            }
        }
    ]
    
    results = list(mongo_db.courses.aggregate(pipeline))
    return json.loads(json_util.dumps(results))

@app.route('/init-db')
def init_db():
    # Initialize PostgreSQL database
    db.drop_all()
    db.create_all()
    
    # Execute SQL script
    with open('app/scripts/postgresql_script.sql', 'r') as f:
        sql_script = f.read()
    
    conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
    cursor = conn.cursor()
    cursor.execute(sql_script)
    conn.commit()
    cursor.close()
    conn.close()
    
    # Initialize MongoDB database
    insert_sample_data()
    
    return jsonify({'message': 'Databases initialized successfully'})
