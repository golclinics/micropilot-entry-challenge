def count_zeros(arr)-> int:
    zero_count = 0
    for n in arr:
        if n == 0:
            zero_count += 1
    print(zero_count)
    return zero_count



arr = [1,2,3,9,3,0,3,30,23,0,00,0,00000,12,] 
arr1 = [] 
arr2 = [1,2,4,5,6] 
count_zeros(arr)# expect 3 zeros - 3
count_zeros(arr1)#expect no zeros - 0
count_zeros(arr2)#expect no zeros - 0
