#!/usr/bin/env python3


def count_zeros(arr):
    """Counts zeros in an array

    Given an array of integers the function will count and return the number
    of zeroes contained in the array.

    Args:
        arr (list): A list of integer values.

    Returns:
        int: The number of zeros contained int the integer array.

    """

    # Counter variable
    count = 0

    # Loop through array while comparing and counting
    for num in arr:
        if num == 0:
            count += 1

    # Return the value of count
    return count


# Tesing th Funtion
# Call the function
arr = [1, 0, 2, 0, 3, 0, 3, 0]

print(count_zeros(arr))
