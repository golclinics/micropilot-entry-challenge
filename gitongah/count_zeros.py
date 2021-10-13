import numpy as np

arr = np.array([1, 0, 5, 6, 0, 2])

number_of_zeros=np.count_nonzero(arr==0)

print(number_of_zeros)