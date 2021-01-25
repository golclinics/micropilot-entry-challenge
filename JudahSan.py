
#!/usr/bin/env python3

def getX(a,b,c):

	# Calculate the value of second part
	d = c * 1.0 - (b * b / (4.0 * a))

	# Print the values
	if (a > 0) :

		# Open upward parabola function
		print("Maxvalue =", "Infinity")


	elif (a < 0) :

		# Open downward parabola function
		print("Maxvalue = ", d)


	else :

		# If a=0 then it is not a quadratic function
		print("Not a quadratic function")


if __name__ == "__main__" :
	a = int(input("Enter the coefficients of a: "))
	b = int(input("Enter the coefficients of b: "))
	c = int(input("Enter the coefficients of c: "))

	getX(a, b, c)
