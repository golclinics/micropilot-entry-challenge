import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

dis = math.sqrt((b**2 - 4*a*c))

l = (-b + dis)/(2*a)
h = (-b - dis)/(2*a)

print(f'x = {l if l > h else h}') 
