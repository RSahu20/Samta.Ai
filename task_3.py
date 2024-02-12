""" Task 3: MySQL Database Operations with Python """

import mysql.connector
  
# connection to the MySQL database
def connect_to_database():
    try:
        db_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="academic_records"
        )
        return db_connect
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None


# Creates the students table in the database
def create_students_table(mycursor):
    create_table_query = """
    CREATE TABLE students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
    """
    mycursor.execute(create_table_query)


# Insert a new student table record
def insert_student_record(mycursor, student_data):
    student_query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    mycursor.execute(student_query, student_data)


# Update the grade of the student with starting first name "Alice"
def update_student_grade(mycursor, new_grade, first_name):
    update_query = """
    UPDATE students
    SET grade = %s
    WHERE first_name = %s
    """
    mycursor.execute(update_query, (new_grade, first_name))

# Delete the student with last name "Smith"
def delete_student_by_lastname(mycursor, last_name):
    delete_query = "DELETE FROM students WHERE last_name = %s"
    mycursor.execute(delete_query, (last_name,))


# Fetch and display all student records
def fetch_all_students(mycursor):
    mycursor.execute("SELECT * FROM students")
    students = mycursor.fetchall()

    print("Student Records:")
    for student in students:
        print(student)

def main():
    db_connect = connect_to_database()
    if db_connect:
        mycursor = db_connect.cursor()

        create_students_table(mycursor)

        student_data = ("Alice", "Smith", 18, 95.5)
        insert_student_record(mycursor, student_data)

        update_student_grade(mycursor, 97.0, "Alice")

        delete_student_by_lastname(mycursor, "Smith")

        fetch_all_students(mycursor)

        # Close cursor and db_connect
        mycursor.close()
        db_connect.close()

if __name__ == "__main__":
    main()
