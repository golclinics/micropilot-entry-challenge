import cmath

def quadratic_func(a, b, c):
    num = cmath.sqrt(pow(b,2) - (4*a*c))
    return (-b + num) / (2*a), (-b - num) / (2*a)

def getX(a, b, c):
    x1, x2 = quadratic_func(a, b, c)
    return print(f"\nMax value is {max(x1.real, x2.real)}")

if __name__ == "__main__":
    a = float(input("Enter (a) value\n"))
    b = float(input("Enter (b) value\n"))
    c = float(input("Enter (c) value\n"))
    getX(a, b, c)