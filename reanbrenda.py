# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def getx(a,b,c):
    squarev = b * b - (4 * a * c)
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
