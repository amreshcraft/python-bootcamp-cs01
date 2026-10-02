import mysql.connector as mysql 

def connect_to_database(host="",user="",password="",database=""):
    try:
        connection = mysql.connect(host=host, user=user, password=password, database=database)
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
        
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")