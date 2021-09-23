from functools import reduce

def count_zeros(arr):
    zeros = list(filter(lambda x: x == 0, arr))
    return len(zeros)
