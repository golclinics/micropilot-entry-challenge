# Given a, b, c for a quadratric expression ax2 + bx + c = 0.
# Write a function getX that returns the larger of the values for X,
# i.e. given x1 = -2 and x2 = 5, getX should return 5.

# Formulas
# x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
# x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)

# Solution.

import math

# set 3 params
def getX(a,b,c):

    try:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) ; x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        if (x1 > x2): print('x1:', x1)
        else: print('x2:', x2)
    except ValueError: print("Impossible, No square root of a negative number")

getX(2, 101, 14)
