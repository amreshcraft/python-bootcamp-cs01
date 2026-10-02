import model.dbconnect as dbconnect
import model.dboperation as dboperation
import controller.studentcontroller as studentcontroller


dbconnection = dbconnect.connect_to_database(host="localhost",user="amresh",password="1234",database="students")

# roll_number = int(input("Enter the roll number of the student: "))
# result =   dboperation.getStudentByRollNumber(roll_number, dbconnection)

# print(result)

# student_data = studentcontroller.createStudent()
# dboperation.addStudent(student_data, dbconnection)

getStudentData = dboperation.getAllStudents(dbconnection)

for student in getStudentData:
    studentcontroller.displayStudent(student)