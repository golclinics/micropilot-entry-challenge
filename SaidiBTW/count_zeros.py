def count_zeros(A):
    count = 0
    for element in A:
        if element == 0:
            count += 1
    return count

print(count_zeros([0, 2, 0, 4, 0]))