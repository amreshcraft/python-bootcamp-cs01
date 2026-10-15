# last digit  = n % 10 

n =  int(input("Enter a number:  ")) # 1+2+3+4+5 = 15

sum = 0
while(n > 0 ) :
   ld = n % 10 
   sum = sum + ld   
   n = n // 10 


print("Sum of digits : ", sum)
