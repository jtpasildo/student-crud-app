from db import getAllStudents, addStudent, updateStudentEmail, deleteStudent

# print function to display each CRUD operation
def print_students(operation):
    print(f"\n {operation}")
    rows = getAllStudents()
    if not rows:
        print("no students found")
        return
    
    print("ID | First Name | Last Name | Email                       | Enrolled")
    print("----------------------------------------------------------------------")
    for r in rows:
        student_id, first_name, last_name, email, enrollment_date = r
        print(f"{student_id:<2} | {first_name:<10} | {last_name:<9} | {email:<27} | {enrollment_date}")
    

def main():
    #1 Initial Setup
    print_students("Initial rows")
    input("Press Enter to show Initial Rows")
    
    #2 Insert
    new_email = f"jordan.pasildo@example.com"
    new_id = addStudent("Jordan", "Pasildo", new_email, "2023-09-03")
    print(f"\n Insert student {new_id} with email {new_email}")
    print_students("After INSERT")
    input("Press Enter to show INSERT")
    
    #3 Update
    updated_email = f"jordan.p@example.com"
    updated = updateStudentEmail(new_id, updated_email)
    print(f"\n Rows updated: {updated}. Student {new_id} updated email to {updated_email}")
    print_students("After UPDATE")
    input("Press Enter to show UPDATE")
    
    #4 Delete
    deleted = deleteStudent(new_id)
    print(f"\n Rows deleted: {deleted}. Student {new_id}")
    print_students("After DELETE")
    input("Press Enter to show DELETE")


if __name__ == "__main__":
    main()
