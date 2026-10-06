def pro_read(filename, mode='r'):
    try:
        with open(filename, mode) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found/mili."
   

def pro_write(filename, content):
    try: 
         with open(filename, 'w') as file:
             file.write(content)
             print(f"Content written to {filename} successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found/mili.")


def copy_binary_file(source, destination):
    try:
       rename = input("Enter the new name for the copied file (with extension): ")
       with open(f"{destination}/{rename}", 'wb') as file :
           file.write(source)
           print(f"Binary content copied to {destination} successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source}' was not found/mili.")