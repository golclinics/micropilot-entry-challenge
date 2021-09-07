def CountZeros(A):
    return len([i for i in A if i==0])

    
assert CountZeros([1, 0, 5, 6, 0, 2]) == 2
assert CountZeros([1,0,0, 0, 5, 6, 0, 2]) == 4
assert CountZeros([1, 0, 5,50,0,6,7, 0, 2]) == 3
