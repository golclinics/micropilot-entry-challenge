import cmath


def is_valid_values(a, b, c):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(a, (int, float))


def compute_roots(a, b, c):

    discriminant = cmath.sqrt((b ** 2) - (4 * a * c))

    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)

    return x1, x2


def getX(a, b, c):

    if not is_valid_values(a, b, c):
        raise ValueError("Value of a, b and c must be of type in or float")
    elif a == 0:
        raise ValueError("Value of a cannot be 0")

    x1, x2 = compute_roots(a, b, c)

    return max(x1.real, x2.real)


if __name__ == "__main__":

    while True:
        try:
            a = float(input("Enter value of a \n"))
            b = float(input("Enter value of b \n"))
            c = float(input("Enter value of c \n"))

            print(getX(a, b, c))
            break
        except ValueError as e:
            print("Exception:", e)
            print("Not a valid value.. Please try again..")
