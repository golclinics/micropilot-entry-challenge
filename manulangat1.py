import math 


def getX(a,b,c):
    # check if a is 0 to prevent zero division error( this can also be handled using a zero division error exception)
    if a == 0 :
        return "Zero division error"
    discriminant = ((b*b)  - (4 * a * c))
    if discriminant >= 0:
        x1=(-b+(math.sqrt(discriminant)))/(2*a)
        x2=(-b-(math.sqrt(discriminant)))/(2*a)
        return max(x1,x2)

    return "Oops! cannot find square root of a negative number!!"
    
print(getX(1,-8,-10))