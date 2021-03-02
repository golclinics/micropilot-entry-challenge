myArray = [1, 0, 5, 6, 0]
 
def count_zeros(A):
    count = 0
    for i in A:
        if i == 0:
             count += 1
    print(count)
count_zeros(myArray)