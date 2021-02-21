
# 

def count_zero(A):
    count = 0
    for i in A:
        if i == 0:
            count += 1

    return count


mylist = [1, 0, 5, 6, 0, 2]
print(count_zero(mylist))