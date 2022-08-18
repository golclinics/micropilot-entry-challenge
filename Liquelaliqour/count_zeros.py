Bdef CountZeros(A):
    count = 0
    for i in A:
        if i == 0:
            count += 1
    return count
