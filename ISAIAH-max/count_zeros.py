# This function count zeros in an Array with numeric values
def count_zeros(A):
    counter = 0
    for i in A:
        if i == 0:
            counter += 1
    print("Array A has", counter, "zero(s)")