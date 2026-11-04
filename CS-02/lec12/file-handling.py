# read , write
f = None
try:
    f = open("about2.txt","r")
    print(f.read())
except FileNotFoundError:
    print("Nahi mili file") 
finally:
    if(f):
       f.close()
       
print("I am Important message")