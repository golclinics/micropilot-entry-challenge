import numpy as np

arr_1d = np.array([3, 0, 5, 2, 0, 0, 8, 6])

# count zeros in 1d array
n_zeros = np.count_nonzero(arr_1d==0)
# display the count of zeros
print(n_zeros)