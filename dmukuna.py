from math import  sqrt, pow

def getX(a, b, c):
    x1 = (-b + sqrt(pow(b, 2) - (4 * a * c)))/(2*a)
    x2 = (-b - sqrt(pow(b, 2) - (4 * a * c)))/(2*a)

    x = 0
    if x1 >= x2:
        x = x1
    else:
        x = x2

    return  x

