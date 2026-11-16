
# 4 Types 

# 1 . Function with no arguments and no return value - TNRN
def greet():
    print("Hello, welcome to the program!")
    

greet()  # Calling the function - Output: Hello, welcome to the program!

# 2. Function with arguments and no return value - TSRN
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program!")

greet_user("Alice")  # Calling the function - Output: Hello, Alice! Welcome to the program!
greet_user("Bob")    # Calling the function - Output: Hello, Bob! Welcome to the program!
res = greet_user("Charlie")  # Calling the function - Output: Hello, Charlie! Welcome to the program!

print(res)  # Output: None (since the function does not return any value)


# 3. Function with no arguments and a return value - TNRV
def get_greeting():
    return "Hello, welcome to the program!"

greeting = get_greeting()  # Calling the function
print(greeting)  # Output: Hello, welcome to the program!


# 4. Function with arguments and a return value - TSRV
def get_user_greeting(name):
    return f"Hello, {name}! Welcome to the program!"

greeting = get_user_greeting("Alice")  # Calling the function
print(greeting)  # Output: Hello, Alice! Welcome to the program!