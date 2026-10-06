# Project - 1 
# Expense Tracker

database = []

def addExpense():
    title = input("Enter expense title: ")
    price = int(input("Enter price: "))
    database.append({
        "id" : "ET-"+title[1],
        "title":title,
        "price":price
    })

def editExpense():
    pass

def removeExpense():
    pass

def getTotalExpense():
    sum = 0
    for i in range(len(database)):
        sum = sum + database[i]["price"]
    return sum

def display():
    print("Expense List Start!!!")
    print("-----------------------------------")
    for  i in range(len(database)):
          print("ID    : ",database[i]["id"])
          print("Title : ",database[i]["title"])  
          print("price : ",database[i]["price"])
          print("____________________________________________")
    print("-----------------------------------")
    print("Expense List End!!!")
      


code = -1
while(code != 0):
    print("Enter 0 for exit expense")
    print("Enter 1 for add expense")
    print("Enter 2 for Edit expense")
    print("Enter 3 for Remove expense")
    print("Enter 4 for Display Expense")
    print("Enter 5 for get total Expense")
    code = int(input())
    if(code == 0):
        print("Exiting...")
        break
    elif(code == 1):
        addExpense()
    elif(code ==2):
        editExpense()
    elif (code == 3):
        removeExpense()
    elif(code == 4):
        display()
    elif (code == 5):
        print("Total Expense : ", getTotalExpense())
    else:
        print("Invalid code !! Please try again")
    