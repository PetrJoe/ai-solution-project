// MongoDB script for creating the University Course Management System database

// Drop existing collections
db.students.drop();
db.courses.drop();
db.departments.drop();

// Create departments collection with embedded faculty
db.departments.insertMany([
  {
    name: "Computer Science",
    building: "Tech Building",
    budget: 500000.00,
    faculty: [
      {
        id: "F20001",
        name: "Robert Johnson",
        email: "robert.johnson@example.com",
        date_of_birth: new Date("1980-03-10"),
        address: {
          street: "789 Oak St",
          city: "Cambridge",
          state: "MA",
          zip: "02139"
        },
        hire_date: new Date("2015-08-15"),
        specializations: ["Artificial Intelligence", "Machine Learning"]
      }
    ]
  },
  {
    name: "Mathematics",
    building: "Science Hall",
    budget: 350000.00,
    faculty: [
      {
        id: "F20002",
        name: "Mary Williams",
        email: "mary.williams@example.com",
        date_of_birth: new Date("1975-11-28"),
        address: {
          street: "101 Pine St",
          city: "Boston",
          state: "MA",
          zip: "02118"
        },
        hire_date: new Date("2010-01-10"),
        specializations: ["Number Theory", "Algebra"]
      }
    ]
  },
  {
    name: "Physics",
    building: "Science Hall",
    budget: 400000.00,
    faculty: []
  }
]);

// Create courses collection with embedded department info
db.courses.insertMany([
  {
    code: "CS101",
    title: "Introduction to Programming",
    description: "Basic programming concepts using Python",
    credits: 3,
    department: {
      name: "Computer Science",
      building: "Tech Building"
    },
    prerequisites: [],
    students_enrolled: []
  },
  {
    code: "CS201",
    title: "Data Structures",
    description: "Advanced data structures and algorithms",
    credits: 4,
    department: {
      name: "Computer Science",
      building: "Tech Building"
    },
    prerequisites: ["CS101"],
    students_enrolled: []
  },
  {
    code: "MATH101",
    title: "Calculus I",
    description: "Introduction to differential calculus",
    credits: 4,
    department: {
      name: "Mathematics",
      building: "Science Hall"
    },
    prerequisites: [],
    students_enrolled: []
  },
  {
    code: "PHYS101",
    title: "Physics I",
    description: "Mechanics and thermodynamics",
    credits: 4,
    department: {
      name: "Physics",
      building: "Science Hall"
    },
    prerequisites: ["MATH101"],
    students_enrolled: []
  }
]);

// Create students collection with embedded enrollment info
db.students.insertMany([
  {
    student_id: "S10001",
    name: "John Smith",
    email: "john.smith@example.com",
    date_of_birth: new Date("1995-05-15"),
    address: {
      street: "123 Main St",
      city: "Boston",
      state: "MA",
      zip: "02115"
    },
    enrollment_date: new Date("2020-09-01"),
    major: "Computer Science",
    enrollments: [
      {
        course_code: "CS101",
        course_title: "Introduction to Programming",
        enrollment_date: new Date("2020-09-05"),
        grade: "A"
      },
      {
        course_code: "CS201",
        course_title: "Data Structures",
        enrollment_date: new Date("2021-01-20"),
        grade: "B+"
      }
    ]
  },
  {
    student_id: "S10002",
    name: "Jane Doe",
    email: "jane.doe@example.com",
    date_of_birth: new Date("1997-08-22"),
    address: {
      street: "456 Park Ave",
      city: "Boston",
      state: "MA",
      zip: "02116"
    },
    enrollment_date: new Date("2021-01-15"),
    major: "Mathematics",
    enrollments: [
      {
        course_code: "MATH101",
        course_title: "Calculus I",
        enrollment_date: new Date("2021-01-20"),
        grade: "A-"
      },
      {
        course_code: "PHYS101",
        course_title: "Physics I",
        enrollment_date: new Date("2021-01-20"),
        grade: "B"
      }
    ]
  }
]);

// Update courses with enrolled students
db.courses.updateOne(
  { code: "CS101" },
  { $push: { students_enrolled: { student_id: "S10001", name: "John Smith", grade: "A" } } }
);

db.courses.updateOne(
  { code: "CS201" },
  { $push: { students_enrolled: { student_id: "S10001", name: "John Smith", grade: "B+" } } }
);

db.courses.updateOne(
  { code: "MATH101" },
  { $push: { students_enrolled: { student_id: "S10002", name: "Jane Doe", grade: "A-" } } }
);

db.courses.updateOne(
  { code: "PHYS101" },
  { $push: { students_enrolled: { student_id: "S10002", name: "Jane Doe", grade: "B" } } }
);
