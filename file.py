file = None
try:
   file = open("abc.txt","r")
   print("File opened successfully.")
   data = file.read()
   print(data)

   print("File read successfully.")
except FileNotFoundError as e:
   print("Error: The file was not found.", e)
finally:
    if(file):
        file.close()
    print("must be executed whether exception occurs or not")

print("important code after file handling")

