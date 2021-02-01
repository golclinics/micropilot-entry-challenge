import cmath


def compute_roots(a, b, c):

    discriminant = cmath.sqrt((b ** 2) - (4 * a * c))

    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)

    return x1, x2


def getX(a, b, c):

    x1, x2 = compute_roots(a, b, c)

    return max(x1.real, x2.real)
