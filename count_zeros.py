#!/usr/bin/env python3

def Count_zeros(arr_A):
    """Count_zeros function returns the number of zeros
       in an array and returns none if the array is empty"""
    num_of_zeros = 0
    #EDGECASE1 checks if the parameter passed is an array
    if type(arr_A) is not list:
        raise TypeError("only array allowed")
    #EDGECASE2 of checking whether the array is empty
    elif len(arr_A) == 0:
        return "None"
    #EDGECASE3: of checking whether 0 is in array
    elif 0 not in arr_A:
        return "No 0's in arr_A"
    #proceeds to counting number of 0's after passing the individual edgecases
    else:
        for num in arr_A:
            if num == 0:
                num_of_zeros += 1
    return num_of_zeros

print(Count_zeros([]))
print(Count_zeros([0, 1, 2, 3, 0]))
print(Count_zeros([1, 2, 3]))
print(Count_zeros(1))
