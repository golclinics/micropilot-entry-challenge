def CountZeros(A):
    A.sort()
    zero_count=0
    for i in a:
        if i==0:
            zero_count+=1
        elif i>0:
            break
    return zero_count



def CountZeros1(A):
    zero_count=0
    for element in A:
        if element==0:
            zero_count+=1   
    return zero_count



