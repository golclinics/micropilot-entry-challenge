def sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum 

#print(sum([2,4,6])) 

def max(arr):
    for i in range(len(arr)):
        max = arr[i]
        for j in range(1,len(arr)):
            if arr[i] < arr[j]:
                max = arr[j]
    return max 

#print(max([2,8,12,6])) 
# recursive count function
def count(arr):
    if len(arr) == 0:
        return 0
    return 1 + count(arr[1:])
print(count([2,8,12,6]))                  



