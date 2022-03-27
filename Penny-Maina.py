import math

def getX(a, b, c):
    n = ((b*b) - 4*a*c)
    
    if(n<0):
        print("Math error!")
        
    else:
        x1 = (-b + math.sqrt(n))/(2*a)
        
        x2 = (-b - math.sqrt(n))/(2*a)
        
        if(x1 > x2):
            print(x1)
        else:
            print(x2)

