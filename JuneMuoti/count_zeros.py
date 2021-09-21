def count_zeros(arr):
    # initialize a counter for keeping count of number of zeros
    zeros_counter=0
    # Loop through the array and increment the counter whenever you come across a zero
    for i in arr:
        if i == 0:
            zeros_counter+=1
    # return the zeros counter
    return zeros_counter

print(count_zeros([[1, 0, 5, 6, 0, 2]]))




