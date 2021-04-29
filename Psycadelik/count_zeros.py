# Big-O complexity: O(N)
def CountZeros(A):
    return A.count(0)


assert CountZeros([1, 0, 5, 6, 0, 2]) == 2
assert CountZeros([3, 0, 9]) == 1

