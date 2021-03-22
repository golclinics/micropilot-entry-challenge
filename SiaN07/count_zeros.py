def countZeros(A):
	count = 0
	for i in A:
		if i == 0:
			count =+ 1;
	print(count)

countZeros([1, 0, 5, 6, 0, 2])