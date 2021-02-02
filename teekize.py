import math


def validate_constants(val):
    if isinstance(val, int) or isinstance(val, float):
        return val
    else:
        raise ValueError("Wrong input {}, value should be an int or float").format(val)


def getX(a, b, c):
    a = validate_constants(a)
    b = validate_constants(b)
    c = validate_constants(c)

    if a == 0:
        raise ValueError("Value of a cannot be zero")

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
    try:
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))
    except Exception as e:
        print(e)

    print(getX(a, b, c))