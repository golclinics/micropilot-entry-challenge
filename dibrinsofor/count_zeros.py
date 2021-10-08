# Write a function CountZeros(A) that takes in an array of integers A, 
# and returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

def count_zeros(A):
    d = 0
    for i in A:
        if i == 0:
            d += 1
    return d

#alternative solution
def count_zeros2(A):
    return A.count(0)


# A = [1, 0, 0, 0, 0, 2]
# print(count_zeros2(A))
# B = [1, 0, 5, 6, 0, 2]
# print(count_zeros(B))