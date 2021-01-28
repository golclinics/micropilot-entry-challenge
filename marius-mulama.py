import math

#Function getX that returns the larger of the values for X
def getX(a, b, c):
    discriminant = pow(b,2) - (4*a*c)
    denominator = 2*a

    if discriminant > 0: #when there are two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) /denominator
        root2 =  (-b - math.sqrt(discriminant))/denominator

        largest_root =  max(root1, root2)

    elif discriminant == 0: #when there are two real and equal roots
        root1 = root2 = -b/denominator
        largest_root = root1

    else: 
        largest_root = 0 #when roots are complex numbers

    return largest_root