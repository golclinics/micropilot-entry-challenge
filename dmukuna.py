from math import sqrt, pow


def getX(a, b, c):
    x1 = (-b + sqrt(pow(b, 2) - (4 * a * c)))/(2 * a)
    x2 = (-b - sqrt(pow(b, 2) - (4 * a * c)))/(2 * a)

    return round(max(x1, x2), 2)


def test():
    assert getX(1, -2, -24) == 6
    assert getX(1, -4, 4) == 2
    assert getX(1, 1.4, 0.45) == -0.5


if __name__ == "__main__":
    test()
    print("Tests passed")
