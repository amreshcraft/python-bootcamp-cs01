import pickle

# Function 1: WriteFile() to input records and write to binary file "STUD.DAT"
def WriteFile():
    with open("STUD.DAT", "wb") as f:
        while True:
            admission_number = int(input("Enter Admission Number: "))
            name = input("Enter Name: ")
            total_mark = float(input("Enter Total Marks: "))
            
            record = [admission_number, name, total_mark]
            pickle.dump(record, f)
            
            choice = input("Do you want to enter more records? (Y/Yes): ").strip().lower()
            if choice not in ['y', 'yes']:
                break
    print("Records successfully written to STUD.DAT.")


# Function 2: ReadFile() to process and display records from "STUD.DAT"
def ReadFile():
    remedial_students = []
    bright_student_count = 0
    
    try:
        with open("STUD.DAT", "rb") as f:
            while True:
                try:
                    record = pickle.load(f)
                    admission_number, name, total_mark = record
                    
                    if total_mark <= 250:
                        remedial_students.append(record)
                    else:
                        bright_student_count += 1
                except EOFError:
                    break  # End of file reached
    except FileNotFoundError:
        print("Error: File 'STUD.DAT' does not exist.")
        return

    # Display REMEDIAL STUDENT LIST
    print("\nREMEDIAL STUDENT LIST")
    print("-" * 35)
    if remedial_students:
        for stud in remedial_students:
            print(f"Adm No: {stud[0]}, Name: {stud[1]}, Marks: {stud[2]}")
    else:
        print("No remedial students found.")

    # Display count of Bright Students
    print("-" * 35)
    print(f"Number of Bright Students (marks > 250): {bright_student_count}")