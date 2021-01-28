# Given a, b, c for a quadratric expression ax2 + bx + c = 0.
#  Write a function getX that returns the larger of the values for X, 
#  i.e. given x1 = -2 and x2 = 5, getX should return 5.

print("Python function")

a= float(input("Input value of a: "))
b= float(input("Input value of b: "))
c= float(input("Input value of c: "))

def getX ():
    y = ((-b)+((b**2)-(4*a*c))**(1/2))/(2*a)
    z = ((-b)-((b**2)-(4*a*c))**(1/2))/(2*a)
    if y>z:
        x = y
        return x
    elif z>y:
        x = z
        return x
    else :
        print("n/a")

print( getX(), "is the larger value of x" )
print("exit")