'''
Python solution that solves a quadratic equation.
ax(square) +bx + c = 0
'''

import math
def getX(a, b , c):
    # Calculuate the dicriminant -> b**b - 4ac
    dis =  (b**2) - (4*a*c) 

    x1 = (-b + (math.sqrt((dis)))) / (2*a)
    x2 = (- b - (math.sqrt((dis))))/ (2*a)

    if x1 > x2:
        return x1

    if x2 > x1:
        return x2

getX(-2, 5, 3)