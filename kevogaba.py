import math


# function for finding roots
def getX(a, b, c):

    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # find the values of X
    ans1 = ((-b + sqrt_val)/(2 * a))
    ans2 = ((-b - sqrt_val)/(2 * a))

    # returning the larger value
    if ans1 > ans2:
        return print(ans1)
    else:
        return print(ans2)


# getting input
# getting rid of ValueError
try:
    a = int(input('Input a: '))
    b = int(input('Input b: '))
    c = int(input('Input c: '))
except ValueError:
    print("Invalid input")

try:
    if a == 0:
        print("Input correct quadratic equation")
    else:
        getX(a, b, c)
except NameError:
    print("Invalid input")
