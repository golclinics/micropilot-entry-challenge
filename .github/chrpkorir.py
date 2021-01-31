import math
def getX(a,b,c):
    try:
        temp = math.sqrt((math.pow(b,2))-(4*a*c))
        ansA=(-b-temp)/(2*a)
        ansB=(-b+temp)/(2*a)
        if ansA>ansB:
            return ansA
        else:
            return ansB

    except ValueError:
        return None


ans= getX(6,12,3)
if ans:
    print(ans)
else :
    print("no answer")  