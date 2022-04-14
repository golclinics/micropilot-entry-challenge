from math import sqrt


def getX(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        num_roots = 2
        x1 = (((-b) + sqrt(discriminant)) / (2 * a))
        x2 = (((-b) - sqrt(discriminant)) / (2 * a))
        print(max(x1,x2))
    elif discriminant == 0:
        num_roots = 1
        x = (-b) / 2 * a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")


getX(-2, 4, 6)
