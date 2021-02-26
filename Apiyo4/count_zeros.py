"""
Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
input                   output
-----                   ------
[1, 0, 5, 6, 0, 2]          2

Pseudocode
----------
1. create a function CountZeros that take in a array  A of integers
2. create a variable count that holds the number of times 0 occurs in an array  and instantiate with a 0
3. loop through the array
4. if 0 occurs in the array, add 1 to the count
5. return count
"""
# Time complexity = O(n) space complexity = O(1)
def CountZeros(A):
    count= 0
    for i in range (len(A)):
        if A[i] == 0:
            count += 1
    return count
print(CountZeros([1, 0, 5, 6, 0, 2]  )) #output = 2
