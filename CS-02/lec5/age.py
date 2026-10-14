age = int(input("Enter your age: "))
# int -> "56" ---> 56

# Falsy Value = 0, False , [] , {}, (), ""
# Truthy Value = all non falsy value is truthy value

if(age > 18):
    print("Adult")
elif(age == 18):
    print("Rukk ja bhai thode din")
else:
    print("Not Adult")