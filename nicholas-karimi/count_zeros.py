# A program to count the number of 0's in a given array

def countZeros(A):
    count = 0
    for number in A:
        if number == 0:
            count += 1
    return count

print(countZeros([1, 0, 5, 6, 0, 2]))
