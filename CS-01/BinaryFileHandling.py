try:
    with open("trees.jpg", "rb") as file:
        fileData = file.read()
        rename = input("Enter the name of the new file (with extension): ")
        with open(f"images/{rename}", "wb") as destination:
            destination.write(fileData)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access the file.")