# Write a function CountZeros(A) that takes in an array of integers A, and 
# returns the number of 0's in that array. 
# For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

def CountZeros(A):
    return A.count(0)


if __name__ == "__main__":
    A = [1, 0, 5, 6, 0, 2]
    print(CountZeros(A))