def firstZero(A,low,high):
    while(low<=high):
        mid = int((high + low) / 2)
        if (( mid == 0 or A[mid-1] == 1)
                      and A[mid] == 0):
            return mid
        if (A[mid] == 1):
            low = mid+1
        else:
            high = mid-1
    return -1
def NumberOfZeroes(A, n):
    ans = firstZero(A,0,n-1)
    if ans == -1:
        return 0
    else:
        return (n-ans)
A = [1, 1, 0, 0, 0, 0, 0, 0]
n = len(A)
print("Number of Zeroes =",
        NumberOfZeroes(A, n))






