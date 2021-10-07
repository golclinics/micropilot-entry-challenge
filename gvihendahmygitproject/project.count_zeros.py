
Solution in python

def CountZeros(A):
    count=0
    for elem in A:   # for each element in A
        if elem==0:  # if that element is 0
            count+=1  # then increment the count 
    return count
    
print(CountZeros([1,0,5,6,0,2]))
print(CountZeros([0,0,0,0,0]))