def CountZeros(A):
    if type(A).__name__ == 'list':
        # initialize count which hold the value of the number of 0s found in array
        count = 0
        #loop through each value of the array and dtermine if zero is ecountered
        for el in A:
            if el == 0:
                count += 1 #increament count
        return print(count)
    else:
        #return an error indicating that input data is invalid
        return print("Please suppply data of type list")

#test
CountZeros([3,4,0,5,8,4,0,12,0]) #returns 3 because there are three zeros

#time complixity O(n) where n is the size of the input array
#space complexity O(1) is constant we are only storing in variable count which uses very minmal space.
