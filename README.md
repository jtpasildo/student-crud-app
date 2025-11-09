## Jordan Pasildo
## 101288061

### Student CRUD Application
This project demonstrates how to interact with a PostgreSQL database using Python

The application connects to a 'students' table and performs full CRUD operations:
- **Read:** getAllStudents(): Retrieves and displays all records from the students table.
- **Create:** addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
- **Update:** updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
- **Delete:** deleteStudent(student_id): Deletes the record of the student with the specified student_id.

### Requirements:
Python 3
PostgreSQL or pgAdmin installed and running locally
psycopg2-binary
python-dotenv

Install dependencies:
pip install -r requirements.txt

## Database Setup:
1. Create database in pgadmin

2. Run the .sql scripts in the sql/ folder in pgAdmin:
create_students_table.sql -> creates the table
insert_initial_data.sql -> inserts the three initial rows
Run the SQL scripts in the sql/ folder in pgAdmin or psql:

3. Create a .env file:
PGHOST=localhost
PGPORT=(port number)
PGDATABASE=(db name)
PGUSER=postgres
PGPASSWORD=(pgAdmin password)

## How to Run:

python3 main.py

Demonstrates and prints out all the CRUD operations in action

## Video Link:
https://youtu.be/vQLkCA163ZA

