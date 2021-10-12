# Write a function CountZeros(A) that takes in an array of integers A, 
# and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.


def count_zero_in_array(A):
    # Getting length of array
    arr_size = len(A)

    # Declaring a global variable and initializing to zero
    global count 
    count= 0

    # Looping through the array elements
    for element in range(0, arr_size):
        
       # For any zero value in the element, increase the count number 
       if (A[element] == 0):
           count += 1
           
    # Prints the count of the number of zeros found in the array of elements       
    print("Count: ", count)



# take multiple inputs in array
print("Enter elements in array")
A = [ int(x) for x in input().split()]

print("Array", A)


# Calling the count_zero_in_array method()
count_zero_in_array(A)
