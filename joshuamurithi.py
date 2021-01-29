import  math


def getX(a,b,c):
    # check if a is zero to avoid zeroDivison error
    if (a==0):
        return None
    # calculating the square root
    sqrt = ((b*b)-(4*a*c))
    if (sqrt>=0):
        x1=(-b+(math.sqrt(sqrt)))/(2*a)
        x2=(-b-(math.sqrt(sqrt)))/(2*a)
    if x1>x2:
        return x1
    else:
        return x2
    
    
getX(1,-3,-10)
# print(p)