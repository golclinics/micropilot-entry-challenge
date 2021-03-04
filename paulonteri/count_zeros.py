
def CountZeros(A):
    count = 0

    for num in A:
        if num == 0:
            count += 1
    return count


def test():
    print(CountZeros([0, 0, 0]) == 3)
    print(CountZeros([]) == 0)
    print(CountZeros([0, 2, 4, 5, 0, 6, 5]) == 2)
    print(CountZeros([1, 2, 3, 4]) == 0)


test()
