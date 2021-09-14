def count_zeroes(A):
	if not isinstance(A, list):
		return 0
	
	count = 0
	
	for num in A:
		if num == 0:
			count += 1
	
	return count
