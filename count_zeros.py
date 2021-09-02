import numpy as np

A = [1, 0, 5, 6, 0, 2]
countZeros = np.array([A])


zeros = np.count_nonzero(countZeros == 0)

print(f"There are {zeros} zeros in my array.")


