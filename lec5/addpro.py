# TNRN

# defining a function / defintion of function
def add1():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"Sum of {a} and {b} is: {a + b}")
    # all db code 


def add2():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    return a + b

def add3(a,b):
    print(f"Sum of {a} and {b} is: {a + b}")
    

# computation function
def add4(a,b):
    return a + b 



# bad coding 

def add5(a,b):
    if(a == 0 and b == 0):
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    print(f"Sum of {a} and {b} is: {a + b}")
    return a + b