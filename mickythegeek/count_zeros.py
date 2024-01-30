def CountZeros(A=[]):
    arr_of_zeros = []
    for i in A:
        if i == 0:
            arr_of_zeros.append(i)

    return len(arr_of_zeros)
           

print(CountZeros([88,0,0,0,0,0,0,0,0,6,5,4,3,2,6,6,8,8,89,9,6]))