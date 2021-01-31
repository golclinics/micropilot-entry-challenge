import math
def getX(a,b,c):
    operator=0
    X=[]
    value=math.sqrt((b**2)-(4*a*c))
    while operator<2:
        if value==0:
            x=((-b)+(value))/(2*a)
        else:
            x=((-b)-(value))/(2*a)
        X.append(x)
        operator+=1
    return int(max(X))
    
print(getX(1,2,1))