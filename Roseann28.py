import math
def getX(a,b,c):
    if a==0:
        print("Enter another number other than zero")
    else:
        portion1_a=b**2
        portion1_b=4*a*c
        portion1=(portion1_a)-(portion1_b)
        if portion1 < 0:
            print('mathematical error')
        else:
            sqroot_portion1=math.sqrt(portion1)
            value1=(- b + sqroot_portion1)/(2*a)
            value2=(-b + sqroot_portion1)/(2*a)
            if value1>value2:
                print(value1)
            else:
                print(value2)
a1=int(input('Enter a:'))
b1=int(input('Enter b:'))
c1=int(input('Enter c:'))
getX(a1,b1,c1)