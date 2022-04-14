import math

def quadratic_equation(a,b,c):
    try:
        sqrt = math.sqrt(b**2 - 4*a*c)
        if sqrt > 0:
            x1 = (((-b) + sqrt)/(2*a))     
            x2 = (((-b) - sqrt)/(2*a))
            maximum = max(x1, x2) 
            return("The larger value is {}".format(maximum) ) 
        elif sqrt == 0:
            x = (-b) / 2*a
            return x
        else:
            return "Can't find roots, discriminant is less than 0."
    except Exception as e:
        print("Err: " + str(e))


if __name__ == '__main__':
    try:
        a = float(input("Input the value of a: "))
        b = float(input("Input the value of b: "))
        c = float(input("Input the value of c: "))

        print(quadratic_equation(a, b, c))

    except Exception as e:
        print("Err: " + str(e))
