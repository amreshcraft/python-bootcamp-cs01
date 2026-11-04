# read , write
try:
    with open("about2.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("Nahi mili file") 
print("I am Important message")
