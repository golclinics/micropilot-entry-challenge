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

    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) ; x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)

    print("This equation has two solutions: x1:",x1, " or, x2:",x2)

    if (x1 > x2):
        print('x1:', x1)
    else:
        print('x2:', x2)

getX(2, 10, 4)
