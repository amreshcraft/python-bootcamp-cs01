# python - dictionary / js-> object/Map , java - HashMap, C++ -> map 

# key : value
l = [] # list
t = () # tuple
d = {} # dictionary

print(type(d))
print(type(l))
print(type(t))

t2 = (8,346,322)

# t2[1] = 19 # error - cant update

print(t2[1])

secret = input("Enter secret key")
d2 = {
    "name" :  " Amresh ",
    "secret" : secret
}


print(d2)


shopping   = [
    {
    "title":"ABC",
    "price":34
    },
         {
           "title":"ABC2",
           "price":34
           },  {
               "title":"ABC3",
               "price":64
               },  {
                   "title":"ABC4",
                   "price":687
                   },  {
                       "title":"ABC5",
                       "price":34
                       },  {
                           "title":"ABC6",
                           "price":36
                           },  {
                               "title":"ABC7",
                               "price":346
                               },   
          
          
          ]


sum = 0
for i in range(len(shopping)):
    d = shopping[i]
    sum = sum +d["price"]
    
print("Sum: ",sum)