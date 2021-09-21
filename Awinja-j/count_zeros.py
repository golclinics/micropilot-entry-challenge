"""

Write a function CountZeros(A) that takes in an array of integers A, 
and returns the number of 0's in that array. 
For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2
"""
def zero_counter(arr: list) -> int:
    count=0
    for x in arr:
        if x == 0:
            count+=1
    return count

print(zero_counter([[1, 0, 5, 6, 0, 2]]))