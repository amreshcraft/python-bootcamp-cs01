# # names = ["Amresh","Akanshi", "Muskan -1 ", "Muskan -2 ", "Riya", "Prachi"]

# names = []


# n = int(input("Enter no of names you want to add : "))

# # for i in range(n):
# #     x = input("Enter student name : ")
# #     names.append(x)
    

# print(names)







file = open("./amresh.txt","r")
print(file.read())

f2 = open("./amresh.txt", "a+")
f2.write("\nHello Guys")

print(file.read())




