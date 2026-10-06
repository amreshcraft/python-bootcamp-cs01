
def displayQuery():
    return f"SELECT * FROM user;"


def insert():
    id = int(input("Enter unique id in integer: "))
    name  = input("Enter your name: ")
    age = int(input("Enter your age in integer : "))
    email = input("Enter your email: ")
    
    query = f"INSERT INTO user (id, name, age, email) VALUES ({id}, '{name}', {age}, '{email}');"
    return query