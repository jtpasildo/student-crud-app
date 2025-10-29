import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD")
    )
    
def getAllStudents():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM students ORDER BY student_id;")
        return cur.fetchall()

def addStudent(first_name, last_name, email, enrollment_date):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                    RETURNING student_id;
                    """, (first_name, last_name, email, enrollment_date))
        conn.commit()
        return cur.fetchone()[0] 
    
def updateStudentEmail(student_id, new_email):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
        conn.commit()
        return cur.rowcount
    
def deleteStudent(student_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        return cur.rowcount