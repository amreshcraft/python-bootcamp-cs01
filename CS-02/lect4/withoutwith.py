file = None
try :
     file = open("./demo2.md","r")
     print(file.read())
    
except FileNotFoundError as err :
    print("Kuch galat ho gya!!! : ",err)
finally:
    print("I will be run always either error is happend or not")
    if(file != None):
        file.close()

