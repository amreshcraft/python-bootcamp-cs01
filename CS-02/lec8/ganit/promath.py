

def factorial(n):
    if(n == 0 or n == 1 ) :
        return 1
    if(n < 0 ):
        raise Exception("Negative value is not allowed")
    fact = 1
    while(n > 1):
        fact = fact * n
        n = n -1
    
    return fact