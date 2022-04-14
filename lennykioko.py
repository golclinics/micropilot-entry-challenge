import math


def validate(num):
    if isinstance(num, int) or isinstance(num, float):
        return num
    else:
        raise ValueError(f"Wrong input {num}, value should be an int or float")


def getX(a, b, c):
    a = validate(a)
    b = validate(b)
    c = validate(c)

    if a == 0:
        raise ValueError("Value of 'a' cannot be zero")

    disc = (b ** 2) - (4 * a * c)  # discriminant

    if disc < 0:
        return "Equation has no real solution"
    elif disc == 0:
        sol = (-b - math.sqrt(disc)) / (2 * a)
        return sol
    elif disc > 0:
        sol1 = (-b - math.sqrt(disc)) / (2 * a)
        sol2 = (-b + math.sqrt(disc)) / (2 * a)
        return max(sol1, sol2)


if __name__ == '__main__':
    try:
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))

        print(getX(a, b, c))

    except Exception as e:
        print(e)
