# Solving the quadratic equation ax**2 + bx + c = 0
import math  

def getx(a,b,c):

    #a= float(input("Enter value of a: "))
    #b= float(input("Enter value of b: "))
    #c= float(input("Enter value of c: "))

 
	d=4

	e=b*b
	f=d*(a*c)

	sqrt=math.sqrt(e-f)

	x1=((-b+sqrt)/(2*a));

	x2=((-b-sqrt)/(2*a));

	#printing  the values 

	print("x1 is",x1)

	print("x2 is",x2)


	#comparison


	if(x1 > x2):

	   print("x1 is greater")

	else:

		print("x2 is greater")




getx(2,12,4)