def CountZeros(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += 1
    return count
    
arr = [1, 0, 5, 6, 0, 2]

print(CountZeros(arr))