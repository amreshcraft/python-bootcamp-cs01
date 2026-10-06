

def insertStudent(student):
    return (
        f"INSERT INTO chhatr (name, class, rollno, english, physics, maths, chemistry, cs, obtained, max_marks, percentage) "
        f"VALUES ('{student['name']}', {student['class']}, {student['rollno']}, {student['english']}, "
        f"{student['physics']}, {student['maths']}, {student['chemistry']}, {student['cs']}, "
        f"{student['obtained']}, {student['max_marks']}, {student['percentage']});"
    )


def getByRollNumberQuery(roll_number):
    return f"SELECT * FROM chhatr WHERE rollno = {roll_number};"

def getAllStudentsQuery():
    return "SELECT * FROM chhatr;"