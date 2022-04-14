import math

def getX(a, b, c):
    dis = math.sqrt((b**2) - (4*a*c))
    l = (-b + dis)/(2*a)
    h = (-b - dis)/(2*a)
    return l if l > h else h

if __name__ == '__main__':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    print(getX(a, b, c))
