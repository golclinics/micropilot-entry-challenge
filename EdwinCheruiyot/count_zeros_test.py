import count_zeros #Import count_zero module in order to use CountZero function
import random #Import random library
A=[] # initalize an array called A
for i in range(0,9): # Loop through a given range of numbers
    A += [random.randint(0,9)] # Add a random integer to the array initalized as A
print("Test Array: ",A)    # Print the array 
count_zeros.CountZeros(A) # Call the count function to get the number of times integer Zero is present in the array
