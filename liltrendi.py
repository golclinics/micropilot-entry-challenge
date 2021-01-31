# Given a, b, c for a quadratric expression ax2 + bx + c = 0. Write a function getX that returns the larger of the values for X, i.e. if x1 = -2 and x2 = 5, getX should return 5.

import math

def getX(a, b, c):
    x1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2 * a)
    x2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2 * a)
    return max(x1, x2)

result = getX(1, 3, -4)
print(result)

