
try :
    with open("Data.txt","r") as file :
        # bata = input("Enter the data to write in the file: ")
        # file.write(bata)    
        fileData = file.read()
        print(fileData)
except FileNotFoundError :
    print("The file does not exist.")
except PermissionError :
    print("You do not have permission to access the file.")