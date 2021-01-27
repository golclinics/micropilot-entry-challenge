import cmath

def quadratic_expression(a, b, c):
    num = cmath.sqrt(pow(b,2) - (4*a*c))
    denom = 2*a

    return (-b + num) / denom, (-b - num) / denom


def getX(a, b, c):
    X1, X2 = quadratic_expression(a, b, c)
    
    return max(X1.real, X2.real)

def tests():
    assert getX(5, 3, 3) == -0.3 
    assert getX(1, -4, 6.25) == 2
    assert getX(5, 2, 1) == -0.2

if __name__ == "__main__":
    tests()
    print("Tests passed!")
