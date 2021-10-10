# Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array.
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

# Naive solution
"""
def CountZeros(A):
    count = 0
    for i in A:
        if i == 0:
            count += 1
    return count
"""

# pythonic solution
def CountZeros(A):
    return A.count(0)
