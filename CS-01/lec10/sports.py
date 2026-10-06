import csv

# St_Id,St_Name,Game_Name,Result
def Accept():
    sid = int(input("Enter student id : "))
    sname = input("Enter student name: ")
    gameName = input("Enter game name: ")
    gameResult = input("Enter game result: ")
    try:
            with open("Result.csv","a") as file :
                writer = csv.writer(file)
                #  header
                if( not isHeaderAlreadyWritten()):
                            writer.writerow(['St_Id','St_Name','Game_Name','Result'])
                writer.writerow([sid,sname,gameName,gameResult])
              
    except FileNotFoundError:
            print("File is not found ")     
    


def isHeaderAlreadyWritten():
    try:
            with open("Result.csv","r") as file :
                reader = csv.reader(file)
                for row in reader :
                    if(row) :
                        return True
                    else:
                        return False
                                           
    except FileNotFoundError:
            print("File is not found ")     


def  Display():
    try:
        with open("Result.csv","r") as file :
            reader = csv.reader(file)
            for row in reader :
                    print(row)
    except FileNotFoundError:
        print("File is not found ")     



def wonCount():
      try:
            with open("Result.csv","r") as file :
                reader = csv.reader(file)
                next(reader)  # pointer + 1 
                c = 0
                for row in reader :
                       if(row[3].lower() == "won") :
                           c = c + 1
                return c
      except FileNotFoundError:
            print("File is not found ")  