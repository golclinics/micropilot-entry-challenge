#!/usr/bin/python3
def CountZeros(array):
    counter = 0 #Initializing count to zero
    for x in array:
        if x == 0:
            counter += 1
    return counter

test = CountZeros([1, 4, 5, 6, 0, 2])
print(test)