import math
def getX(a, b, c):
    x1  = (-(b) + (math.sqrt((b*b) - (4 * a * c))))/(2 * a)
    x2 = (-(b) - (math.sqrt((b*b) + (4 * a * c))))/(2 * a)
    return x1 if x1 > x2 else x2
