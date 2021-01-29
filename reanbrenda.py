
import math


def getx(a,b,c):
    if a == 0:
        return None
        # calculating the square root
    squarev = b * b - (4 * a * c)
    if squarev >= 0:
        x1 = (-b - math.sqrt(squarev)) / (2 * a)
        x2 = (-b + math.sqrt(squarev)) / (2 * a)
    if x1 < x2:
        print(x2)
    else:
        print(x1)


if __name__ == '__main__':
    a = 1
    b = 10
    c = -24
    getx(a, b, c)
