def CountZeros(A):
    how_many_zeros = 0
    for i in A:
        if i == 0:
            how_many_zeros += 1

    return how_many_zeros
