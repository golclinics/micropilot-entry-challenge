def binary_search(numbers, item):
    low = 0
    high = len(numbers) -1
    """ if len(numbers) == 0 or len(numbers) ==1:
        return "Search not possible" """
    while low <= high:
        mid = (low + high)
        myguess = numbers[mid]
        if myguess == item:
            return mid
        elif myguess > item:
            high = mid -1 
        else:
            low = mid + 1       
    return None
mylist =[1,2,3,4,5]
print(binary_search(mylist,1))
