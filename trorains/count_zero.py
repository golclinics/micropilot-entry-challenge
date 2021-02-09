def CountZeros(A):
    list_zero=[]
    for n in A:
        if n == 0:
         list_zero.append(n)
        count_zero = len(list_zero)
    return count_zero

A =[1, 0, 5, 6, 0, 2]
print(CountZeros(A))