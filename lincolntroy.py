import math  


def getx(a,b,c):
	
	# a = int(input("Enter a number a: "))
	# b = int(input("Enter a number b: "))
	# c = int(input("Enter a number c: "))

	d=4

	e=b*b
	f=d*(a*c)

	bigsqrt=math.sqrt(e-f)

	x1=((-b+bigsqrt)/(2*a));

	x2=((-b-bigsqrt)/(2*a));

	#print the values here

	print("Value 1 is",x1)

	print("Value 2 is",x2)

	#now compare which is greater


	if(x1 > x2):

		print("Value 1 greater")

	else:

		print("Value 2 greater")




getx(2,12,4)


