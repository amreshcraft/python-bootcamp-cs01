import mysql.connector

try:
    # Attempt connection to your database engine
    connection = mysql.connector.connect(
        host="localhost",
        user="amresh",
        password="1234"  # Replace with the password you set up earlier
    )
    
    if connection.is_connected():
        print("🚀 Successfully connected to the MySQL database!")
        connection.close()

except Exception as e:
    print(f"❌ Connection failed: {e}")
