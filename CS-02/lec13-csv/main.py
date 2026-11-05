import csvpro as cp

print("===========================================================")
print(" CSV World ")
print("===========================================================")
students = cp.get_all_students()

studentId = int(input("Enter student ID: "))
name = input("Enter student name: ")
email = input("Enter student email: ")
age = int(input("Enter student age: "))

# list
student = [studentId, name, email, age]

cp.add_student(student)

id = int(input("Enter student ID to search: "))
student = cp.get_student(id)
if(student):
    print("Student found: ", student)
else:
    print("Student not found.")