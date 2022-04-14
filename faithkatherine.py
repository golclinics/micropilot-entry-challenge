import math
def getX():
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
           firstvalue = (-b + sqrtvalue)/ (2*a)
           secondvalue = (-b - sqrtvalue)/ (2*a)

           if firstvalue > secondvalue:
               print(firstvalue)
            
           else:
                print(secondvalue)
           
    else:
        print("a should not be zero")
    
    return

getX()


    
    
   
