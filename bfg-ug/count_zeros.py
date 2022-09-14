def CountZeros(A):
    count = 0

    for x in range(len(A)):

        if A[x] == 0:
            count=count+1

    return (print(count))




a =[1, 0, 5, 6, 0, 2]

CountZeros(a)

