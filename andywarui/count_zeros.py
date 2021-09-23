def firstZero(arr, low, high):
  
    if (high >= low):
      
        # Check if mid element is first 0
        mid = low + int((high - low) / 2)
        if (( mid == 0 or arr[mid-1] == 1)
                      and arr[mid] == 0):
            return mid
          
        # If mid element is not 0
        if (arr[mid] == 1): 
            return firstZero(arr, (mid + 1), high)
              
        # If mid element is 0, but not first 0
        else: 
            return firstZero(arr, low, (mid - 1))
      
    return -1
  
# function firstZero()
def countZeroes(arr, n):
  
    # Find index of first zero in given array
    first = firstZero(arr, 0, n - 1)
  
    # If 0 is not present at all, return 0
    if (first == -1):
        return 0
  
    return (n - first)


# Driver Code
arr = [1, 1, 1, 0, 0, 0, 3, 0]
n = len(arr)
print("Count of zeroes is",
        countZeroes(arr, n))