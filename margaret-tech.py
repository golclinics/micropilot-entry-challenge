# Solve quadratic equation using quadratic formula
# Given a, b, c for a quadratric expression ax^2 + bx + c = 0.
# Write a function getX that returns the larger of the values for X
# i.e. if x1 = -2 and x2 = 5, getX should return 5.
# where a≠0


num_a = float(input("Enter value for a: "))
num_b = float(input("Enter value for b: "))
num_c = float(input("Enter value for c: "))

print("a: " + str(num_a) + "  " + "b: " + str(num_b) + "  " + "c: " + str(num_c))

def getX(num_a, num_b, num_c):
    from math import sqrt

    # Discriminant determines number of solutions
    # Discriminant is b^2 - 4ac
    num_disc = ((num_b * num_b) - (4 * num_a * num_c))
    print("num_disc: " + str(num_disc))

    if num_disc > 0:
        sqroot_num_disc = sqrt(num_disc)
        print("sqroot_num_disc: " + str(sqroot_num_disc))

        x1 = ((-num_b + sqroot_num_disc) / (2 * num_a))
        x2 = ((-num_b - sqroot_num_disc) / (2 * num_a))
        
        print("There are two different solutions")
        print("x1 is: " + str(x1))
        print("x2 is: " + str(x2))
        print("Larger value is: " + str(max(x1,x2)))

    elif num_disc == 0:
        x = ((-num_b) / (2 * num_a))
        print("There is only one solution")
        print("x is: " + str(x))
    else:
        print("There is no real solution")
    return;

if num_a == 0:
    print("For a, please enter a number greater or less than 0")
else:
    getX(num_a, num_b, num_c)