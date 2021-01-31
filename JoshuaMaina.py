from math import sqrt


def get_max_x(a, b, c):
    try:
        value = b ** 2 - 4 * a * c
        x1 = (-b + sqrt(value)) / (2 * a)
        x2 = (-b - sqrt(value)) / (2 * a)
        return max(x1, x2)
    except TypeError:
        print("Incorrect types used for operation")
        print("All digits are required to be integers")
    except ZeroDivisionError:
        print("The variable a should not be a 0")
    except ValueError:
        print("The root of this equation is an imaginary number")


# Example 1
print(get_max_x(1, 5, 1))

# Example 2
print(get_max_x(1, 2, 1))

# Example 3
print(get_max_x(1, -2, 1))

# Repo example
print(get_max_x(1, -3, -10))
