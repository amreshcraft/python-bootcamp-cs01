
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try :
    c = a / b
    print("The result of the division is: ", c)
except ZeroDivisionError :
    print("You cannot divide a number by zero. Please enter a valid number."+ str(ZeroDivisionError) )   


print("Very important code that should run after the exception handling block.")