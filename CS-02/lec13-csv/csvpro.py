import csv

# list of student records
def add_student(student):
    try :   
        with open("students2.csv","a",newline="") as f:
             writer = csv.writer(f)
             writer.writerow(student)
             raise Exception("Simulated error for testing purposes.")  # Simulate an error for testing
             
    except FileNotFoundError:
        print("File not found: Unable to write to the file. Please check if the file exists.")
    except PermissionError:
        print("Permission denied: Unable to write to the file. Please check if the file is open in another program.") 
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")        
    print("Student added successfully!")





def get_student(id):
       with open("students.csv","r") as f:
            reader = csv.reader(f)
            for row in reader :
                if row[0] == str(id):
                    return row
            return None

def get_all_students():
    with open("students.csv","r") as f:
        reader = csv.reader(f)
        for row in reader :
            print(row)
    


