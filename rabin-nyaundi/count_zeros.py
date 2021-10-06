def count_zero(arr):
    result_arr = []
    for i in arr:
        if i == 0:
            result_arr.append(i) 
    return result_arr


result = count_zero([1,2,3,0,0,0,8])
assert len(result) == 3
print("Test 1 passed")


result = count_zero([0,0,0,0,0,0,])
assert len(result) == 6
print("Test 2 passed")

result = count_zero([])
assert len(result) == 0
print("Test 3 passed")