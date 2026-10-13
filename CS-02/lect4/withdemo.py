try :
     with  open("./demo.md","r") as file :
         print(file.read())
except FileNotFoundError as err :
    print("Kuch galat ho gya!!! : ",err)
