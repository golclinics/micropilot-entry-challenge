# Python program to get largest X of quadratic equation by Robert NGABO MUGISHA
import math 

# function for getting root(largest X) 
def getX( a, b, c): 
    x1 = int((- b + math.sqrt(b * b - 4 * a * c))/2*a)
    x2 = int((- b - math.sqrt(b * b - 4 * a * c))/2*a)
    if x1 > x2:
        return x1
    elif x2 > x1:
        return x2

#Init data 
a = 1
b = -1
c = -6

# If a is 0, then incorrect equation 
if a == 0: 
    print("unsolvable quadratic equation")
else: 
	print(getX(a, b, c))
