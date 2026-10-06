
try:
   with open("abc.txt","r") as file:
     print("File opened successfully.")
     data = file.read()
     print(data)

   print("File read successfully.")
except FileNotFoundError as e:
   print("Error: The file was not found.", e)


print("important code after file handling")

