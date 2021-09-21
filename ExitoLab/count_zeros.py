# The functions accept array A and print out the occurence of 0's
def CountZeros(A):
    if (len(A) == 0 or not A):
        return("The array can not be empty")
    
    counter = 0
    filterValue = 0
    for number in A:
        if str(number).isdigit() == False:
            return ("The array contains a negative value:" + number + " only parse integer arrays")
        if (number == filterValue):
            counter+=1
    return counter

A = [1, 0, 5, 6, 0, 2, 0, 0, 1, 2,0]
print(CountZeros(A))