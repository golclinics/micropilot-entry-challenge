
print("before")

#the formula is x = (-b+-((b*2)-(4ac))**(1/2)))/(2a)
a= float(input("Enter value of a: "))
b= float(input("Enter value of b: "))
c= float(input("Enter value of c: "))

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
print("end")
