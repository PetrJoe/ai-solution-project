# University Course Management System

A Flask-based application demonstrating the implementation of a University Course Management System using both PostgreSQL (object-relational) and MongoDB (NoSQL document store) databases.

## Project Overview

This project was developed to address the requirements of a database systems assessment, focusing on comparing relational and NoSQL document store database technologies. The application implements a University Course Management System that tracks students, courses, departments, and enrollments.

### Key Features

- **Object-Relational Implementation** using PostgreSQL with:
  - Inheritance hierarchies (Person → Student/Faculty)
  - Array types for prerequisites and specializations
  - User-defined types for addresses
  - Triggers for data validation

- **NoSQL Document Store Implementation** using MongoDB with:
  - Embedded documents for related entities
  - Arrays for storing related data
  - Denormalization to reduce the number of collections
  - Document-oriented design patterns

- **Comparison Interface** showing:
  - Database schema differences
  - Query approaches
  - Performance characteristics
  - Critical analysis of both approaches

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- MongoDB 4.4 or higher

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/PetrJoe/ai-solution-project.git
   cd ai-solution-project
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure database connections:
   
   Create a `.env` file in the project root with the following content:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://username:password@localhost/dbcomparison
   MONGO_URI=mongodb://localhost:27017/dbcomparison
   ```

5. Initialize the databases:
   
   Start the application and navigate to the "Initialize Databases" link, or run:
   ```
   flask run
   ```
   Then visit: http://localhost:5000/init-db

## Project Structure

```
ai-solution-project/
├── app/
│   ├── __init__.py          # Flask application initialization
│   ├── routes.py            # API and view routes
│   ├── models/
│   │   ├── postgresql_models.py  # PostgreSQL ORM models
│   │   └── mongodb_models.py     # MongoDB models and functions
│   ├── scripts/
│   │   ├── postgresql_script.sql # SQL script for PostgreSQL setup
│   │   └── mongodb_script.js     # JavaScript for MongoDB setup
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css         # Application styling
│   │   └── img/
│   │       └── uml_diagram.png   # UML class diagram
│   └── templates/
│       ├── index.html            # Home page template
│       └── comparison.html       # Database comparison template
├── config.py                # Application configuration
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Database Design

### UML Class Diagram

The UML class diagram represents the data model independent of the database implementation, showing the main entities and their relationships:

- **Person** (base class)
  - **Student** (inherits from Person)
  - **Faculty** (inherits from Person)
- **Department**
- **Course**
- **Enrollment** (association class)

### PostgreSQL Implementation

The PostgreSQL implementation uses object-relational features:
- Inheritance for the Person-Student-Faculty hierarchy
- Array types for prerequisites and specializations
- User-defined types for addresses
- Triggers for data validation

### MongoDB Implementation

The MongoDB implementation uses document store features:
- Faculty embedded within departments
- Enrollments embedded within students
- Department information embedded within courses
- Arrays for prerequisites, specializations, and enrolled students

## API Endpoints

- `/` - Home page
- `/comparison` - Database comparison page
- `/init-db` - Initialize both databases
- `/api/postgresql/students` - List all students from PostgreSQL
- `/api/postgresql/complex-query` - Run a complex query in PostgreSQL
- `/api/mongodb/students` - List all students from MongoDB
- `/api/mongodb/complex-query` - Run a complex query in MongoDB

## Critical Discussion

The project includes a critical discussion comparing the PostgreSQL and MongoDB implementations, focusing on:
- Data modeling approaches
- Schema design differences
- Query complexity
- Performance characteristics
- Use cases for each database type

## License

This project is for educational purposes only.

## Author

PetrJoe

## Acknowledgments

- University of Sunderland
- Database Systems Module
