def firstZero(arr, low, high):
    """
    once the array is sorted all elements are present bfore the zero assuming there are no negative numbers
    """
 
    if (high >= low):
     
        # Check if mid element is first 0
        mid = low + int((high - low) / 2)
        if (( mid == 0 or arr[mid-1] != 0)
                      and arr[mid] == 0):
            return mid
         
        # If mid element is not 0
        if (arr[mid] != 0):
            return firstZero(arr, (mid + 1), high)
             
        # If mid element is 0, but not first 0
        else:
            return firstZero(arr, low, (mid - 1))
     
    return -1

def countZeroes(arr):
    """
    wrapper for firstzero fuctions
    credit to geeksforgeeks.org for starter code
    arr is the input array
    """
    counter = 0
    #sort the array
    arr.sort(reverse=True)
    print(arr)
    n = len(arr)
    print(n)

    # Find index of first zero in given array
    first = firstZero(arr, 0, n - 1)
 
    # If 0 is not present at all, return 0
    if (first == -1):
        return 0

    for i in range(first,len(arr)):
        if (arr[i] == 0):
            counter += 1
        else:
            break

    return counter


# Test code
arr = [1, 0, 5, 6, 0, 2, -1]

print("Count of zeroes is",countZeroes(arr))

