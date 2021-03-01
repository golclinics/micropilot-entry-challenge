def Count_zeros(arr_A):
    """Count_zeros function returns the total number of zeros
       in an array and returns none if the array is empty"""
    zeros_arr = []
    #CORNERCASE1 checks if the parameter passed is an array
    if type(arr_A) is not list:
        raise TypeError("only array allowed")
    #CORNERCASE2 of checking whether the array is empty
    elif len(arr_A) == 0:
        return "None"
    #CORNERCASE3: of checking whether 0 is in array
    elif 0 not in arr_A:
        return "No 0's in arr_A"
    #proceeds to counting number of 0's after passing the individual cornercases
    else:
        for number in arr_A:
            if number == 0:
                zeros_arr.append(number)
    return len(zeros_arr)

print(Count_zeros([]))
print(Count_zeros([0, 1, 2, 3, 0]))
print(Count_zeros([1, 2, 3]))
print(Count_zeros(1))
