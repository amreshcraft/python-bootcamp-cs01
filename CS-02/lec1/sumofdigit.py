# 456345324325435 = 4 + 5 + 6 + 3 + 4 + 5 + 3 + 2 + 4 + 3 + 2 + 5 + 4 + 3 + 5 = 54
# 
x = int(input("Enter a number: "))
sum = 0


while(x > 0 ):
   ld = x % 10  # give last digit
   sum = sum + ld # sum last digit to previous sum
   x = x // 10  # remove last digit





print("Sum of digits is: ", sum)