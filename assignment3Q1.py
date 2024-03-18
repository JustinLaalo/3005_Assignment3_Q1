import psycopg2

# Database connection parameters from pgadmin
DB_NAME = 'Assignment3'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'


# Function to make database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

# Function to get all students
def get_all_students(cur):
    
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    
    return students

# Function to add a student
def add_student(first_name, last_name, email, enrollment_date,cur):
    
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
   

# Function to update student email
def update_student_email(student_id, new_email,cur):
    
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
   

# Function to delete a student
def delete_student(student_id,cur):
    
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    

# Function to display menu and handle user input
def main_menu():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("Create Table students(student_id SERIAL Primary Key,first_name Text Not Null, last_name Text Not Null, email Text Not Null Unique ,enrollment_date Date)")
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",('John', 'Doe', 'john.doe@example.com', '2023-09-01'))
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'))
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02'))

    while True:
        print("\nMain Menu:")
        print("1. Show all students")
        print("2. Insert a student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_students(cur)
        elif choice == '2':
            add_new_student(cur)
        elif choice == '3':
            update_student_email_menu(cur)
        elif choice == '4':
            delete_student_menu(cur)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        connection.commit()
    cur.close()
    connection.close()

# Function to display all students
def display_all_students(cur):
    students = get_all_students(cur)
    print("\nStudents:")
    for student in students:
        print(student)

# Function to add a new student
def add_new_student(cur):
    print("Insert a New Student:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    enrollment_date = input("Enrollment date (YYYY-MM-DD): ")
    add_student(first_name, last_name, email, enrollment_date,cur)
    print("Student added successfully.")

# Function to update student email
def update_student_email_menu(cur):
    student_id = input("Enter student ID to update email: ")
    new_email = input("New email: ")
    update_student_email(student_id, new_email,cur)
    print("Student email updated successfully.")

# Function to delete a student
def delete_student_menu(cur):
    student_id = input("Enter student ID to delete: ")
    delete_student(student_id,cur)
    print("Student deleted successfully.")

if __name__ == '__main__':
    main_menu()