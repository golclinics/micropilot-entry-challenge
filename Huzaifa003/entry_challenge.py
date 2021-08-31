def CountZeroes(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count = count + 1
    return count


array = [1, 0, 5, 6, 0, 2]
print(CountZeroes(array))