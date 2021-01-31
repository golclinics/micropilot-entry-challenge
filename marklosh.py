import math

def get_x(a, b, c):
     discriminant = (b**2) - (4 * a*c)
     sqrt_val = math.sqrt(abs(discriminant))
     # magnitude = math.sqrt(abs(sqrt_val**2 + (-b/2a)**2))
     if discriminant > 0:
         val_of_x1 = (-b-math.sqrt(discriminant))/(2 * a)
         val_of_x2 = (-b + math.sqrt(discriminant))/(2 * a)
         if val_of_x1 > val_of_x2:
             return val_of_x1
         return val_of_x2
     elif discriminant == 0:
          return -b / (2*a)
     else:
         return (- b / (2 * a), "+ j", sqrt_val/2*a), (- b / (2 * a), " - j", sqrt_val/2*a)

get_x(1, 6, 40)
