def count_zeros(intarr):
    count = 0
    for item in range(0, len(intarr)):
        if intarr[item] == 0:
            count = count + 1
    return count

arr = [1, 0, 5, 6, 0, 2]

print (count_zeros(arr))