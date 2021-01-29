from cmath import sqrt
import  math
def getX(a,b,c):
    result = []
    q = b**2 - 4*(a*c)
    root = math.sqrt(abs(q))
    try:
        if q>0:
            x1 = -b - root / (2*a)
            x2 = -b + root / (2*a)
            result.append(x1)
            result.append(x2)
            print("the max of x1 and x2 is :")
            print(max(result))
            
        elif q == 0:
            print("One root")
            x = -b / (2*a)
            result.append(x)
            print(x)
        else:
            print("No real root Roots")  
    except ZeroDivisionError:
        print("Input correct quadratic equation") 
        

  
getX(30,10,-3)  
