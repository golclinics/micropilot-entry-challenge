# Write a function CountZeros(A) that takes in an array of integers A, 
# and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.


def count_zero_in_array(A):

    # counting number of zeros      
    print("Count of zeros: ",  A.count(0))



# take multiple inputs in array
print("Enter elements in array")
A = [ int(x) for x in input().split()]

print("Array", A)


# Calling the count_zero_in_array method()
count_zero_in_array(A)