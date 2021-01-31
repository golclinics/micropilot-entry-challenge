import cmath

a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))

# calculating  the discriminant
dis = (b ** 2) - (4 * a * c)

# find two results
ans1 = (-b - cmath.sqrt(dis)) / (2 * a)
ans2 = (-b + cmath.sqrt(dis)) / (2 * a)

print(ans2)
print(ans1)
def getX():

    if int(ans2.imag) > int(ans1.imag):
        print(f"ans2 {ans2} is greater")
    else:
        print(f"ans1{ans1} is greater")
getX()