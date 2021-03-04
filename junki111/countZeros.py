def countZeros(A):
    count = 0
    for elem in A:
        if elem == 0:
            count += 1

    return count

arr = [1,0,2,0,3,0]
print(countZeros(arr))
    
