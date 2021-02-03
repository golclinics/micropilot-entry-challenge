
# Given a, b, c for a quadratric expression ax2 + bx + c = 0.
# Write a function getX that returns the larger of the values for X,
# i.e. given x1 = -2 and x2 = 5, getX should return 5.



# Solution.

import math

def getX(a,b,c):

    try:

        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) 

        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)

        X = max(x1,x2)

        print(X)


        
    except ValueError: print("Unless complex numbers are required which cant be compared , there are no real numbers to square roots of negative numbers ")



getX(8, 16, 1)


getX(2, 2, 1)
