
1
Assignment Two
Due 16 May by 23:59Points 65Submitting a file uploadAvailable after 17 Mar at 0:00
Start Assignment
Important Information
This is the second assignment for this module and is worth 65% of the overall module mark.All work must be done individually.The following learning outcomes will be assessed:1. Demonstrate critical appreciation of current and new data models and database systems for
traditional and Big Data systems.2. Appraise current and emerging trends in database systems and their application in the real world.3. Design and develop database systems using a range of different database development tools.4. Evidence of critical evaluation of the major developments and issues of databases within the
database arena and their support in various application areas.You are required to submit your work within the bounds of the University Infringement of Assessment
Regulations (see the Student Handbook
(https://services.sunderland.ac.uk/academicregistry/studenthandbook/) ).  Plagiarism, paraphrasing and
downloading large amounts of information from external sources, will not be tolerated, and will be dealt
with severely.  You should make full use of any source material, which would normally be an occasional
sentence and/or paragraph (referenced) followed by your own critical analysis/evaluation.  You will
receive no marks for work that is not your own. Your work may be subject to checks for originality which
can include use of an electronic plagiarism detection service.Where you are asked to submit an individual piece of work, the work must be entirely your own.  The
safety of your assessments is your responsibility.  You must not permit another student access to your
work.Where referencing is required, unless otherwise stated, the Harvard referencing system must be used
(see your Programme Guide).Please ensure that you retain a duplicate of your assignment.  We are required to send samples of
student work to the external examiners for moderation purposes.  It will also safeguard in the unlikely
event of your work going astray.
Assignment Requirements
Your assignment is to design, develop and query a database using multiple DBMS's, i.e., PostgreSQL
and MongoDB, to provide a brief comparison of relational and NoSQL document store database
3/24/25, 11:33 AM Assignment Two
https://canvas.sunderland.ac.uk/courses/75448/assignments/165770 1/8
technologies. 
If you are at an off-campus centre and have been using Oracle then you may use Oracle instead of
PostgreSQL for this assignment.
Use of any other DBMS than those specified above will result in a mark of zero where appropriate.For a case study of your choice, perform the following tasks:1. Provide a UML class diagram (NOT an ER diagram) showing the main entities and attributes in your
design and the relationships between them. The UML class diagram MUST be data model
independent, i.e., you are showing potential entities in the system, NOT tables.  Ensure that you
include complex relationships (e.g., inheritance hierarchies, aggregation, etc.) in your design.  Provide
a 200 word critical discussion outlining your rationale for embedding of complex relationships in your
scenario.  Ensure you correctly cite all references that you have used.2. Create a complete SQL script file that will run in PostgreSQL to implement the design from task 1 as
an OBJECT-RELATIONAL database.  Make sure you make full use of object features, e.g., arrays,
inheritance, temporal data, etc.).  A purely relational database will be marked at most as Major Errors. Ensure your SQL script file runs without errors, i.e.:a. it efficiently drops then creates the database objects (tables, user defined types, stored
procedures, triggers, etc.),b. implements suitable data integrity constraints (using both constraints as well as triggers), andc. inserts sufficient sample data for your queries below.Make sure that you provide the complete SQL script file within your submitted report, with a .sql
extension.  Any auto-generated code exported from the DBMS or any other tool will be given a mark
of 0 for this part, and may lead to an academic misconduct investigation. 3. Develop a set of documents using MongoDB to develop the equivalent document store database for
your design in task 1.  Ensure you make use of appropriate document store features including, for
example, nested documents, arrays, temporal data, etc.  Do not simply replicate the PostgreSQL
implementation but make full use of MongoDB document store features.  Make sure the sample
data you use matches the data stored in your database from task 2.  You must provide the complete
script file for creating your MongoDB database (i.e. the collection_name.insert commands), do not just
provide a list of documents outputted from the interface, otherwise you will get 0 marks for this part. 4. Provide a brief critical discussion, of no more than 300 words, identifying and illustrating (i.e. by
including examples) of how you have used MongoDB document store features to convert your
scenario from an object-relational to a NoSQL document store system.  As part of this discussion
explain how you have used NoSQL document store features of MongoDB to provide a suitable NoSQL
system (e.g. how have you reduced the number of collections, how have you used nested documents
and arrays, etc.).  Ensure you correctly cite all references that you have used.
5. Develop the following queries (i.e., SQL SELECT statements) in PostgreSQL on your database from
task 2 above. Provide a short, natural language, description of each query.  Ensure that you develop
queries which include:
a. A join of three or more tables – you must use multiple types of join operations in this
query (e.g., inner join, left/right/full outer joins, etc.) and the query must include a restriction on
3/24/25, 11:33 AM Assignment Two
https://canvas.sunderland.ac.uk/courses/75448/assignments/165770 2/8
