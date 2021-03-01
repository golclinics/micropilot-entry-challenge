def CountZeros(A): # Create a function called A
    count=0 # Initalize the count value
    for i in A: # Create a for loop to get values in the array
        if i == 0: # check if value matches Zero
            count+=1 # count the number of times the value occurs
    print("Number of times Zero occurs: ",count)  #Resulting output printed on console
        
A=[1, 0, 0, 5, 6, 0, 2] # an example array
CountZeros(A) # Function CountZero is called

