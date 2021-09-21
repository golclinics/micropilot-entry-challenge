def CountZeros(A):
    num=0
    for item in A:
        if item==0:
            num+=1
    return num
print(CountZeros([1, 0, 5, 6, 0, 2]))