import math


def getX(a, b, c):
    # discriminant part under square root in the quadratic equation
    disc = (b ** 2) - (4 * a * c)

    # x values
    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)

    return max(x1, x2)


print(getX(-1, 5, 6))