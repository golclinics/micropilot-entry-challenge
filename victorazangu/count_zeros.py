def CountZeros(A):
    numberOfZeros = 0;
    for i in A:
        if i == 0:
            numberOfZeros = numberOfZeros + 1
            
    return numberOfZeros

arr = [1, 0, 5, 6, 0, 2,2,0,0,0]

print(CountZeros(arr))
