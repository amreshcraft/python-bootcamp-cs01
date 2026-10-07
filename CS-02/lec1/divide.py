x = input("Enter a number: ") # number - by default input is string, so we need to convert it into integer
print(type(x)) # <class 'str'>
if(int(x) == 0):
    print("You entered zero (nor positive nor negative)")
elif (int(x) > 0):
    print("You entered a positive number")
elif(int(x) < 0):
    print("You entered a negative number")

    