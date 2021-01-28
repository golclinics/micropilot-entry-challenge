import math

def quadroots(a, b, c):

	if a == 0:

		print("Not a quadratic equation")

	else:

		sqdiff = b * b - 4 * a * c

		sqroot = math.sqrt(abs(sqdiff))

		if sqdiff > 0:
			print((-b + sqroot)/(2 * a))
			print((-b - sqroot)/(2 * a))

		elif sqdiff == 0:
			print("x = " + str((-b/(2*a))))

		else:
			print((-b / 2 * a), " + i",sqroot)
			print((-b / 2 * a ), " - i",sqroot)





