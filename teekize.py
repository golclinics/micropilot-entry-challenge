import math


def validate_coefficients(val):
    if isinstance(val, float) or isinstance(val, int):
        return val
    else:
        raise ValueError("{}, hould be an int or float".format(val))


def getX(a, b, c):
    a = validate_coefficients(a)
    b = validate_coefficients(b)
    c = validate_coefficients(c)

    if a == 0:
        raise ValueError("a, should not be zero")

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant < 0:
        return "Equation has no solution"

    elif discriminant == 0:
        x = (-b - math.sqrt(discriminant)) / (2 * a)
        return x
    elif discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return max(x1, x2)


if __name__ == '__main__': 
    """
    if file is ran directly get some user input
    and test the inputs.
    """
    try:
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))
    except Exception as e:
        print(e)

    print(getX(a,b,c))