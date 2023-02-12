def CountZeros(A):
    ## Checking if the list contains none integer values
    none_int_values = [x for x in A if not isinstance(x, int)]

    if none_int_values:
        raise TypeError("Your list contains none integer values!")

    zeros_count = len([x for x in A if x== 0])
    return zeros_count

zeros = CountZeros([1, 0, 5, 6, 0, 3])

