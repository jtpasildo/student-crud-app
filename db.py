import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Connect to db using credentials in .env file
def get_conn():
    return psycopg2.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD")
    )
    
# Retrieves and displays all records from the students table
def getAllStudents():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM students ORDER BY student_id;")
        return cur.fetchall()

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                    RETURNING student_id;
                    """, (first_name, last_name, email, enrollment_date))
        conn.commit()
        return cur.fetchone()[0] 

# Updates the email address for a student with the specified student_id.   
def updateStudentEmail(student_id, new_email):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
        conn.commit()
        return cur.rowcount

# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        return cur.rowcount