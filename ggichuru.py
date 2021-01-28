import numpy as np

def getX():
    coefficients = [-1,2,5]
    get_roots = np.roots(coefficients)
    max_root = max(get_roots)
    # max_root = int(max_root)
    print("The larger root is: ", max_root)

getX()