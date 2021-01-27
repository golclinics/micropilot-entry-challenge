import cmath
def getX(a,b,c):
    x1 =(-b - cmath.sqrt((b*b)-(4*a*c))) / (2*a)
    x2 =(-b + cmath.sqrt((b*b)-(4*a*c))) / (2*a) 
    ans = max(x1.real,x2.real)
    return (round(ans,2))

def test_code():
    assert getX(1,-1,-6) == 3
    assert getX(1,7,6) == -1
    assert getX(6,5,-6) == 0.67
if __name__ == "__main__":
    test_code()
    print("Everything passed")
