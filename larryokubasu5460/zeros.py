# Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.


def countZeros(array):
    count=0
    for i in range(0,len(array)):
        if array[i] == 0:
            count=count+1
    return count

A=[1,0,5,6,0,2]
zeros_count=countZeros(A)
print(f'Number of zeros is {zeros_count}. in array {A}')
