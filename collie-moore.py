from math import sqrt


def getX(a, b, c):
    d = ((b**2)-(4*a*c))
    x1 = (-b-sqrt(d))/(2*a)
    x2 = (-b+sqrt(d))/(2*a)
    if x1 > x2:
        return x1
    else:
        return x2


print(getX())
