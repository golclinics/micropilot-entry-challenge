def CountZeros(A:list)->int:
    count = 0
    if len(A) != 0:
        for element in A:
            if element == 0:
                count += 1
        return count
    else:
        return count

test1 = [1, 0, 5, 6, 0, 2]
test2 = []
test3 = [1, 2, 3, 4, 5, 6]
test4 = [0, 0, 0]
test5 = ['0', '0', '1', '2']

count = CountZeros(test5)
print(f'Number of zeros in {test5} is {count}')