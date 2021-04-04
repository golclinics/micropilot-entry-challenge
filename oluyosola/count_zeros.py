# Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
def countZeros(array):
    # count declared to be zero
    count=0
    # loop through array length and count the number of zeros
    for m in range(0,len(array)):
        if array[m] == 0:
            count=count+1
    return count
    # testing the function
A = [1, 0, 5, 6, 0, 2]
zeros_count=countZeros(A)
print("Number of zeros is", zeros_count)
