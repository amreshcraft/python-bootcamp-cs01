import csv
try:
    with open("./Student.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if(int(row[1]) < 18):  
                print(row)

except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access the file.")