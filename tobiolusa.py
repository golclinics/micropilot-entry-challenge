def CountZero(*args):
    ''' A function that takes in an array of integers A, and returns the number of 0's in that array.'''
    A = []
    for x in args:
        A.append(x)
    print(f'The number of zero is; {A.count(0)}')
    return A   
# test = CountZero(32, 4, 0, 3, 0, 4, 5)
# print(test)
