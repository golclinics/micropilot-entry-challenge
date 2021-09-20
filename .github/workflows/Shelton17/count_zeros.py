import numpy as np
# build the array
arr = np.array([1, 0, 2, 0, 3, 4, 10, 5])

#count the number of zeros in the array
zero = np.count_nonzero(arr==0)

print(zero)
