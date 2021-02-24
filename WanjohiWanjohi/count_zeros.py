def CountZeros(A):
    """
    A function that takes in an array A and returns the number of 0's in the array
    """
    if type(A) == list:
        zero_count = A.count(0)
        return zero_count
    else:
        raise ValueError('Type of parameter needs to be a list')
my_array = [3,2,4,0,9,1]
CountZeros(my_array)
    