#Write a function CountZeros(A) that takes in an array of integers A, 
#and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

def CountZeros(A):
    z=0
    #print ( A[3])
    for x in A:
        if x == 0:
            z = z+1
    print (z)
    

A=[1, 0, 5, 6, 0, 2]
 
CountZeros(A)