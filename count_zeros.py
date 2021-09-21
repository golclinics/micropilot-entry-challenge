def count_zeros(array):
    return len(list(filter(lambda element: element == 0, array)))


print(count_zeros([1, 0, 5, 6, 0, 2]))
