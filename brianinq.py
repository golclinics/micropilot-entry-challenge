import math


def getX(a, b, c):
    x1 = (-(b) + math.sqrt(b**2 - 4*(a*c)))/(2*a)
    x2 = (-(b) - math.sqrt(b**2 - 4*(a*c)))/(2*a)

    return max(x1, x2)
