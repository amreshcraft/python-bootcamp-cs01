import connectdb as db

# host = input("Enter host: ")
# user = input("Enter user: ")
# password = input("Enter password: ")
# database = input("Enter database name: ")

mydb = db.connecteToDatabase('localhost', 'root', '1234', "hello")
if mydb.is_connected() :
    print("Connection successful!")
else:
    print("Connection failed!")
    
    

    
    

def insertStudent(rollNo, name ,classname,gender):
    cursor = mydb.cursor()
    query = f"INSERT INTO students (rollno,name,class,gender) VALUES('{rollNo}','{name}',{classname},'{gender}');"
    cursor.execute(query)
    mydb.commit()
    print("Student inserted successfully!")
    



rollNo = input("Enter roll number: ")
name = input("Enter name: ")
classname = int(input("Enter class: "))
gender = input("Enter gender: ")

insertStudent(rollNo, name, classname, gender)