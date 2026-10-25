import math

def sin0(n):
    if(n == 0 ) :
        return 0
    elif(n==30):
        return 1/2
    elif(n == 45):
        return 1/math.sqrt(2)
    elif(n==60):
        return math.sqrt(3) / 2
    elif ( n == 90) :
        return 1
    else :
        raise Exception("Not implemented for other values")