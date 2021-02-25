import numpy as np

def CountZeros(A):
    print(np.count_nonzero(A==0))

if __name__ == '__main__':
    print("Enter values to be added into the array leaving a space in between")
    input_numbers = np.array([[int(x) for x in input().split()]])
    print(CountZeros(input_numbers))
