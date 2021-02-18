#!/usr/bin/env python3

def Count_zeros(arr_A):
    """Count_zeros function returns the number of zeros
       in an array and returns none if the array is empty"""
    num_of_zeros = 0
    if len(arr_A) == 0:
        return "None"
    else:
        for num in arr_A:
            if num == 0:
                num_of_zeros += 1
    return num_of_zeros

print(Count_zeros([]))
print(Count_zeros([0, 1, 2, 3, 0]))
