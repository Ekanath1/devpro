
import mysql.connector

class Student:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="testmysql",
        database="mydatabase"
    )

    def __init__(self):

        print('student id should be 1 to 10')
        self.my_cursor = self.mydb.cursor()
    def add_student(self):
        student_id = input("Enter student ID: ")
        sql = """select id from student_record"""
        self.my_cursor.execute(sql)
        students = self.my_cursor.fetchall()
        if (int(student_id),) in students:
            print("Student ID already exists!")
            return

        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        rec = "insert into student_record(Id, name, age, grade) values (%s, %s, %s, %s)"
        val = [(student_id, name, age, grade)]
        self.my_cursor.executemany(rec, val)
        self.mydb.commit()

        print("Student added successfully!")

    def view_students(self):

        sql = """ select * from student_record"""
        self.my_cursor.execute(sql)
        students = self.my_cursor.fetchall()

        if not students:
            print("No students available.")
            return
        print("\nStudent List:")
        for Id, Name, Age, Grade in students:
            print(f"ID: {Id}, Name: {Name}, Age: {Age}, Grade: {Grade}")
        print()

    def update_student(self):
        sql = """ select Id from student_record"""
        self.my_cursor.execute(sql)
        students = self.my_cursor.fetchall()
        st = []
        for stu in students:
            st.append(stu[0])
        print(st)

        student_id = int(input("Enter student ID to update: "))

        if student_id not in st:
            print("Student ID not found!")
            return


        print("Enter new details (leave blank to keep current value):")
        n = input(f"Enter new name (current: {student_id}): ")
        a = int(input(f"Enter new age (current: {student_id}): "))
        g = input(f"Enter new grade (current: {student_id}): ")

        update_query = """
        UPDATE student_record 
        SET name = %s, age = %s, grade = %s 
        WHERE Id = %s
        """

        self.my_cursor.execute(update_query, (n, a, g, student_id))
        self.mydb.commit()
        print("Student information updated successfully!")

    def delete_student(self):
        sql = """ select Id from student_record"""
        self.my_cursor.execute(sql)
        students = self.my_cursor.fetchall()
        st = []
        for stu in students:
            st.append(stu[0])
        print(st)

        student_id = int(input("Enter student ID to delete: "))

        if student_id not in st:
            print("Student ID not found!")
            return

        delete_query = "DELETE FROM student_record WHERE Id = %s"

        self.my_cursor.execute(delete_query, (student_id,))
        self.mydb.commit()
        print("Student information deleted successfully!")

    def menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student \n2. View Students \n3. Update Student \n4. Delete Student \n5. Exit ")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("@@@@@@@@@Invalid choice, please try again.@@@@@@@@")

if __name__ == "__main__":
    sms = Student()
    sms.menu()
