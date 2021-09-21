def countZeros(arr):
    if type(arr) != list:
        return "Enter list of elements"
    elif len(arr) == 0:
        return 0
    
    result = 0

    for i in arr:
        if i == 0:
            result += 1
    
    return result


inputArr = [1,0,3,4,6,0,0,30]
countZeros(inputArr)