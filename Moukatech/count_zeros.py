def countZeros(A):
    count = 0
    for i in A:
        if i == 0:
            count += 1
    return count

A = [1, 0, 5, 6, 0, 2]

print(countZeros(A))

