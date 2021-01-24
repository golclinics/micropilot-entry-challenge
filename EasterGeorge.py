'''

Given a, b, c for a quadratric expression 
ax2 + bx + c = 0. Write a function getX that returns the larger
 of the values for X, i.e. given x1 = -2 and x2 = 5, getX should return 5.
'''
from numpy import sqrt


def getX(a, b, c):
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("x1 = " + str(x1))
    print("x2 = "+str(x2))
    if x1 > x2:
        return x1
    else:
        return x2


# call function and pass values a =1, b=4, c=3
getX(1, 4, 3)
