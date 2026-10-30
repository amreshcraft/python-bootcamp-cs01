import fruitstack as fs

def display(FruitStack):
    if(len(FruitStack) == 0 ) :
        print("EMPTY STACK")
    else:
        print(FruitStack)
        
        
# {'Name':'Apple','Origin':'France','Price':120,
# 'Expiry':'12-08-2025'}
s = 0

while(s != -1):
   name = input("Enter fruit name: ")
   origin = input("Enter origin: ")
   price = int(input("Enter price"))
   expiry = input("Enter expiry: ")
   d = {'Name':name,'Origin':origin,'Price':price,
'Expiry':expiry}
   
   fs.push_fruit(d)
   print("Do you want add other value .. enter any number: ")
   print("Enter -1 to exit")
   s = int(input())




display(fs.FruitStack)
fs.pop_fruit()
display(fs.FruitStack)
   
