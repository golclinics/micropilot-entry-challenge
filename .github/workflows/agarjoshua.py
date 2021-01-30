import cmath
import math 

def getX(a,b,c):
    
    if (a==0):
        return None

    d = (b**2) - (4*a*c)

    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)

    return max(x1.real,x2.real)   

a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))

y = getX(a,b,c)
print(y)