import math
print("Enter the integers for the quadratic equation: ")

a = int(input("enter the first integer: "))
b = int(input("enter the second integer: "))
c = int(input("enter the third integer: "))



def getx():
    d = ((b**2) - (4*a*c))
    if d > 0:
       g = math.sqrt(d)
       e = (- b + g)/(2*a)
       f = (- b - g)/(2*a)
       if f > 0:
        print(f)
       elif e > 0:
        print(e)
       else:
         print("Both values are less than 0")
      
    else:
        print("cannot find sqrt of a negative number")
   
    
   
getx()