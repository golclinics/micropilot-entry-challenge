
def CountZeros(integers):
    """
    :param integers: List of intergers
    :return The number of zeroes in the list
    """
    zeroes_count = 0
    for integer in integers:
        if integer == 0:
            zeroes_count = zeroes_count + 1
    
    return zeroes_count
