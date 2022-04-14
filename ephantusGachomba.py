import math
def getX(a, b , c):
    x1 = (-b + (math.sqrt((b*b) - (4 * a * c)))) / (2*a)
    x2 = (- b - (math.sqrt((b*b) - (4 * a * c))))/ (2*a)
    if x1 > x2:
        return x1

    if x2 > x1:
        return x2

getX(1,-3,-10)