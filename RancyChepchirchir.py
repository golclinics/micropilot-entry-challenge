# import math module 
import math

print('Quadratic equation : (a * x**2) + b*x +c')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

def quadratic(a, b, c):
    # calculate the discriminant 
    discriminant = (b ** 2) - (4 * a * c)

    # roots
    if discriminant > 0:
        num_roots = 2
        x1 = ((-b + math.sqrt(discriminant)) / (2 * a))
        x2 = ((-b - math.sqrt(discriminant)) / (2 * a))
        print('The bigger of the 2 roots: %f ' % (max(x1, x2)))

    elif discriminant == 0:
        num_roots = 1
        x = (-b) / 2*a
        print('There is one root: ', x)

    else:
        num_roots = 0
        print('No roots, discr < 0.')

quadratic(a,b,c)
