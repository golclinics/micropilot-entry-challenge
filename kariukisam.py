def getx(a, b, c):
    """
    Function to return the maximum of the roots in a quadratic equation 
  
    Parameters: 
    a (int): Coefficient of X^2
    b (int): Coefficient of X
    c (int): Constant term
  
    Returns: 
    int: The largest of the two roots
    """
    import cmath #Module for complex numbers operation

    # Finding the discriminant in quadratic function
    d = (b**2) - (4*a*c)

    firstRoot = (-b+cmath.sqrt(d)) / (2*a)
    secondRoot = (-b-cmath.sqrt(d)) / (2*a)

    #For real roots
    if d >= 0:
        #Absolute to eliminate the zero valued imaginary part
        firstRoot = abs(firstRoot)
        secondRoot = abs(secondRoot)

        if firstRoot >= secondRoot:
            largerX = firstRoot

        else:
            largerX = secondRoot
        
    #For complex roots    
    else: 
        if abs(firstRoot) >= abs(secondRoot):
            largerX = firstRoot

        else:
            largerX = secondRoot
        
    return largerX