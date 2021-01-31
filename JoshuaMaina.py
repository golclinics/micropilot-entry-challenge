from math import sqrt


def get_max_x(a, b, c):
    if not (isinstance(a, int) &
            isinstance(b, int) &
            isinstance(c, int)):
        print("One of the values is not an integer")
    else:
        value = b ** 2 - 4 * a * c
        if value < 0:
            print("This leads to an imaginary number as the root")
        else:
            x1 = (-b + sqrt(value)) / (2 * a)
            x2 = (-b - sqrt(value)) / (2 * a)
            return max(x1, x2)


# Example 1
print(get_max_x(1, 5, 1))

# Example 2
print(get_max_x(1, 2, 1))

# Example 3
print(get_max_x(1, -2, 1))

# Repo example
print(get_max_x(1, -3, -10))
