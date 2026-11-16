import mysql.connector as sql 

def getConnection():
    return sql.connect(host="localhost",user="root",password="1234", database="subset")

def Create():
    conn  = getConnection()
    pointer = conn.cursor()
    pointer.execute("""CREATE TABLE captains (
    id int NOT NULL,
    name varchar(50) NOT NULL,
    post varchar(100) NOT NULL
);""")
    print("create table successfully")
    conn.commit()
    pointer.close()


def INSERT_CAPTAINS():
     id = int(input("Enter id: "))
     name = input("Enter apka naam : ")
     post = input("enter your post : ")
     conn  = getConnection()
     pointer = conn.cursor()
     pointer.execute(f"INSERT INTO captains VALUES({id},'{name}','{post}');")
     print("Insertion successfully")
     conn.commit()
     pointer.close()
     


def INSERT():
     id = int(input("Enter id: "))
     name = input("Enter apka naam : ")
     kaksha = int(input("enter your class : "))
     marks = float(input("Enter your marks"))
     conn  = getConnection()
     pointer = conn.cursor()
     pointer.execute(f"INSERT INTO students VALUES({id},'{name}',{kaksha},{marks});")
     print("Insertion successfully")
     conn.commit()
     pointer.close()
     
     
    

# READ

def Read():
   conn = getConnection()
   pointer = conn.cursor()
   pointer.execute("SELECT * FROM students;")
   data = pointer.fetchall() # returns list of tuples
# data = pointer.fetchmany(2) 
# data = pointer.fetchone()
   for item in data :
    if(item[3] < 70):
     print("===============================")
     print("ID : ",item[0])
     print("NAME : ",item[1])
     print("CLASS: ",item[2])
     print("MARKS: ",item[3])
     print("===============================")
     print("fetched successfully")
     conn.close()



# Create()

INSERT_CAPTAINS()