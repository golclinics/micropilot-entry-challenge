import math
def quadratics():
    a = int(input("enter the value of a, it should not be zero:"))
    b = int(input("enter the value of b:"))
    c = int(input("enter the value of c:"))
    
    if a != 0:
       bsquare = b*b
       second = 4*a*c
       if bsquare < second:
           print("These are complex numbers")
       else:
           sqrtvalue = math.sqrt( bsquare - second)
           print("The values of x are")
           print((-b + sqrtvalue)/ (2*a))
           print((-b - sqrtvalue)/ (2*a))
           
    else:
        print("a should not be zero")
    
    return

quadratics()


    
    
   
