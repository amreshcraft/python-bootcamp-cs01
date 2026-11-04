a = 5
b = 0 
print("Starting the program")
try:
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")
print("Very important message")