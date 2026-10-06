
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
  res = a / b
  print(res)
except ZeroDivisionError as e:
   print("Error: Division by zero is not allowed.", e)
else:
    print("The division was successful.")
print("important code after exception handling")
