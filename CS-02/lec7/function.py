# loop vs function 

# 10 lines of code -> multiple times -- loop 
# for i in range(3):
#     print("Hello Python")

# print("Hey Amresh")
# for i in range(7):
#     print("Hello Python")
# 10 lines of code - run when it required -- function 

def fun():     # defining a function / function declaration
      print("Hello Python") 


# fun()  # calling a function / call

# for i in range(5):
#     fun()
    # print("Hello loop")
    
# 1. TN,RN - only for printing/logging
def square1():
    n = int(input("enter a number"))
    print(n * n )
    
# square1()

# 2. TS, RN 
def square2(n):
    print(n * n ,end="  ,")
     
# square2(6)
sq = [5,7,9,11,13]
# for i in range(len(sq)):
#     square2(sq[i])


# 3.TN,RS
def square3():
    n = int(input("enter number :    "))
    return n * n

# a = square3()
# print(a)

# 4. TS,RS 
def square4(n):
    return n * n

# t = square4(9)
# print(t)
def savetodb(s):
    print("data : ",s)
    print("Successffully saved to database")
    
    
    
sq2 = [10,20,30,40,65,78,98,445]
for i in range(len(sq2)):
    s = square4(sq2[i])
    savetodb(s)
    
    

