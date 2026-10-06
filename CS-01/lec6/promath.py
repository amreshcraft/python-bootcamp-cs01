

def power(base , power):
       if(float(base) == float(0)) :
          return 0
       result = 1
       if(float(power) == float(0)) :
          return 1
       while(power):
            result = result * base
            power = power - 1
      
       return result
    
    
# def sqrt(x):
#     return power(x, 0.5)