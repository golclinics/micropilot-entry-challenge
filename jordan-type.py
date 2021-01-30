# Given a, b, c for a quadratric expression ax2 + bx + c = 0.
# Write a function getX that returns the larger of the values for X,
# i.e. given x1 = -2 and x2 = 5, getX should return 5.

# formula  x1=((-b+sqrt)/(2*a))  x2=((-b-sqrt)/(2*a))

# results  x1 = -2 x2 = 5
import math

# set 3 params
def getX(a,b,c):
    # constant value d 
	d=4
	e=b*b
	f=d*(a*c)

	sqrt=math.sqrt(e-f)

	x1=((-b+sqrt)/(2*a))

	x2=((-b-sqrt)/(2*a))


	print("The value for x1 is",x1)

	print("The value for x2 is",x2)


	# if statement to check the greatest


	if(x1 > x2):

	   print("value",  x2, "is larger than", x1 )

	else:

		print("value",  x2, "is larger than", x1)

# testing the function with @ params a, b, c
getX(2,12,4)
