def getX(a,b,c):
    """
    Given a, b, c for a quadratric expression ax2 + bx + c = 0.
    function getX that returns the larger of the values for X,
    i.e. given x1 = -2 and x2 = 5, getX should return 5.
    """
    import numpy as np

    q = (b*b) - (4*a*c)

    x1 = (-b - np.sqrt(q))/(2*a)
    x2 = (-b + np.sqrt(q))/(2*a)

    return max(x1,x2) # returns the largest of its arguments: value closest to positive infinity.
