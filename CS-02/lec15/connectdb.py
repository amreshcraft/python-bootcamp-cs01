import mysql.connector as sql      
        
        
def connecteToDatabase(host = 'localhost', user = 'root', password = '', database='dbname'):
    try : 
      mydb = sql.connect(
      host=host,
      user=user,
      password=password,
      database=database
      )  

      return mydb   
    except Exception as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if mydb.is_connected():
            mydb.close()
            print("MySQL connection is closed")
           
           



