# function takes in an array of integers A and returns the count for zeros in the array

def count_zeros(A)-> int:
    count = 0
    for num in A:
        if num == 0:
            count += 1

    return 0


# Simple function call for dry run
arr = [1, 0, 5, 6, 0, 2]
result = count_zeros(arr)   # 2
print(result)  