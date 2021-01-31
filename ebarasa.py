
import math


def getx(a, b, c,):

    solution = b ** 2 - 4 * a * c

    if solution > 0:

        solution1 = math.sqrt(solution)

        x1 = (-b + solution1) / (2 * a)

        x2 = (-b - solution) / (2 * a)

        print()

        if x1 > x2:
            print(f"X: {x1}")
        else:
            print(f"X: {x2}")

    elif solution == 0:

        print()

        x1 = (-b) / (2 * a) if a != 0 else 0

        print(f"x1 and x2 are same: {x1}")

    else:
        print()
        print("It is not a real quadratic equation!")


print()
print("THIS PROGRAM PRINTS THE LARGEST NUMBER OF A QUADRATIC EQUATION SOLUTION")
print()

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

getx(a, b, c,)

