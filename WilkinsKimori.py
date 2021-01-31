

# Solving a quadratic equation

# import math module

import math

# Entering the coefficients of the equation

print("Enter value a")
a = int(input())

print("Enter value b")
b = int(input())

print("Enter value c")
c = int(input())


# find two solutions
d = pow(b, 2) - (4*a*c)

if(d > 0):
    sol1 = int((-b-math.sqrt(d))/(2*a))
    sol2 = int((-b+math.sqrt(d))/(2*a)) 
    
    if sol1 > sol2:
        greaterRoot = sol1

    else:
        greaterRoot = sol2
    
    print("The greater root is: {0}".format(greaterRoot))

else:
    print("Bruh, we don't do complex numbers here!")
    
    

