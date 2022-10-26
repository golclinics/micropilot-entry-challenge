
from math import sqrt

def getLargestX(a,b,c):
    if b==0:
        return 0
    else:
        numerator = b**2 - 4*a*c
        x1 = (-b + sqrt(numerator))/(2*a)
        x2 = (-b - sqrt(numerator))/(2*a)

        if x1 > x2:
            largest = x1
        else:
            largest = x2
            
    return largest

print(getLargestX(1,6,-9))
