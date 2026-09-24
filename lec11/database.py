import mysql.connector as myd
from mysql.connector import Error
import utils



connection = None
try:
    
    connection = myd.connect(
        host="localhost",
        user="amresh",
        password="1234",
        database="mario"
        )
    
    if(connection.is_connected()):
        print("Successfully connectedd to database!!!!")
        
        with connection.cursor() as pointer :
            # query = utils.insert()
            # print("query: ",query)
            # pointer.execute(query)
            # connection.commit();
            # print("User Inserted Successfully!!!@!")
             readQuery = utils.displayQuery()
             pointer.execute(readQuery)
             users = pointer.fetchall()
             for user in users :
                 print(user)
    

except Error as err:
    print("Database Error: ",err)
    
finally:
    if(connection != None):
        connection.close()