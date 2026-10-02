
# (name,class,rollno,english,physics,maths,chemistry,cs,obtained,max_marks,percentage)

def createStudent():
    name = input("Enter the name of the student: ")
    class_name = input("Enter the class of the student: ")
    rollno = int(input("Enter the roll number of the student: "))
    english = int(input("Enter the marks obtained in English: "))
    physics = int(input("Enter the marks obtained in Physics: "))
    maths = int(input("Enter the marks obtained in Maths: "))
    chemistry = int(input("Enter the marks obtained in Chemistry: "))
    cs = int(input("Enter the marks obtained in Computer Science: "))
    obtained = english + physics + maths + chemistry + cs
    max_marks = 500
    percentage = (obtained / max_marks) * 100

    student = {
        "name": name,
        "class": class_name,
        "rollno": rollno,
        "english": english,
        "physics": physics,
        "maths": maths,
        "chemistry": chemistry,
        "cs": cs,
        "obtained": obtained,
        "max_marks": max_marks,
        "percentage": percentage
    }

    return student
    
    

# def displayStudent(student):
#     if student:
#         print(f"Name: {student[0]}")
#         print(f"Class: {student[1]}")
#         print(f"Roll Number: {student[2]}")
#         print(f"English: {student[3]}")
#         print(f"Physics: {student[4]}")
#         print(f"Maths: {student[5]}")
#         print(f"Chemistry: {student[6]}")
#         print(f"Computer Science: {student[7]}")
#         print(f"Obtained Marks: {student[8]}")
#         print(f"Max Marks: {student[9]}")
#         print(f"Percentage: {student[10]:.2f}%")
#     else:
#         print("Student not found.")    



# def displayStudent(student):
#     if not student:
#         print("\n❌ Student record not found.\n")
#         return

#     # Extract values for readability
#     name, student_class, rollno, eng, phy, math, chem, cs, obtained, max_m, pct = student

#     card = f"""
# ┌──────────────────────────────────────────────────────────┐
# │                   STUDENT MARKSHEET                      │
# ├──────────────────────────────────────────────────────────┤
# │ Name        : {name:<25}                  │
# │ Class       : {student_class:<5}  Roll No : {rollno:<12}           │
# ├──────────────────────────────────────────────────────────┤
# │ SUBJECT MARKS                                            │
# │   • English          : {eng:>3} / 100                            │
# │   • Physics          : {phy:>3} / 100                            │
# │   • Mathematics      : {math:>3} / 100                            │
# │   • Chemistry        : {chem:>3} / 100                            │
# │   • Computer Science : {cs:>3} / 100                            │
# ├──────────────────────────────────────────────────────────┤
# │ SUMMARY                                                  │
# │   • Marks Obtained   : {obtained:>3} / {max_m}                      │
# │   • Percentage       : {pct:>6.2f}%                            │
# └──────────────────────────────────────────────────────────┘
# """
#     print(card)



def displayStudent(student):
    if not student:
        # Red text for error
        print("\033[91m\n❌ Student record not found.\033[0m\n")
        return

    # Color codes
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    name, student_class, rollno, eng, phy, math, chem, cs, obtained, max_m, pct = student

    print(f"\n{BOLD}{CYAN}═══════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}               🎓 STUDENT REPORT CARD              {RESET}")
    print(f"{BOLD}{CYAN}═══════════════════════════════════════════════════{RESET}")
    print(f" {BOLD}Name{RESET}     : {YELLOW}{name}{RESET}")
    print(f" {BOLD}Class{RESET}    : {student_class}    |    {BOLD}Roll No{RESET} : {rollno}")
    print(f"{CYAN}───────────────────────────────────────────────────{RESET}")
    print(f" {BOLD}SUBJECT MARKS:{RESET}")
    print(f"   📘 English          : {eng}/100")
    print(f"   🔬 Physics          : {phy}/100")
    print(f"   📐 Mathematics      : {math}/100")
    print(f"   🧪 Chemistry        : {chem}/100")
    print(f"   💻 Computer Science : {cs}/100")
    print(f"{CYAN}───────────────────────────────────────────────────{RESET}")
    print(f" {BOLD}Total Marks{RESET} : {obtained} / {max_m}")
    print(f" {BOLD}Percentage{RESET}  : {GREEN}{pct:.2f}%{RESET}")
    print(f"{BOLD}{CYAN}═══════════════════════════════════════════════════{RESET}\n")