# Write a function CountZeros(A) that takes in an array of integers A, 
# and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

def CountZeros(A: list) -> int:
    if isinstance(A, list):
        count = 0
        for item in A:
            if item == 0:
                count += 1
        return count
    else:
        return f"Error: '{A}' is not a list/array"
    

# print(CountZeros(0))
# print(CountZeros([]))
# print(CountZeros([1, 0, 5, 6, 0, 2]))
