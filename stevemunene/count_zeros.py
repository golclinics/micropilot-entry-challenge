def main():
    A = [1, 0, 5, 6, 0, 2]
    print('0 has occured {} times'.format(CountZeros(A)))

#count function to count number of 0's in array A
def CountZeros(A):
    return A.count(0)

if __name__ == "__main__":
    main()
