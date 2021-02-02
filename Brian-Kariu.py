import math
def getX(a,b,c):
    #Made an exception in the event of the calculation of square root of a negative number
    try:
        x1 = (-b - math.sqrt(b*b - 4*a*c))/2*a
        x2 = (-b + math.sqrt(b*b - 4*a*c))/2*a
        if x2 > x1:
            return x2
        else:
            return x1
    except ValueError:
        print("Impossible, Can't calculate square root of a negative number")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

print(getX(a,b,c))
