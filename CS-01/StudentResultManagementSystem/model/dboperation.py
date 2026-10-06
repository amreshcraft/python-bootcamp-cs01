import sql.query as query

def getStudentByRollNumber(roll_number, dbconnection):
    pointer = dbconnection.cursor()
    pointer.execute(query.getByRollNumberQuery(roll_number))
    row = pointer.fetchone()
    pointer.close()
    return row

    



def getAllStudents(dbconnection):
    pointer = dbconnection.cursor()
    pointer.execute(query.getAllStudentsQuery())
    rows = pointer.fetchall()
    pointer.close()
    return rows


def addStudent(student_data,dbconnection):
    pointer = dbconnection.cursor()
    pointer.execute(query.insertStudent(student_data))
    dbconnection.commit()  # it store the changes in the database permanently
    pointer.close()
    print("Student added successfully.")


def updateStudent(roll_number, updated_data):
    # Your database update logic here
    pass