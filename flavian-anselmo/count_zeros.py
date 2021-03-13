def CountZeros(N):
    counter=0
    for num in N:
        if num==0:
            counter+=1
    return counter 
def test_algo():
    print(CountZeros([0, 0, 0]) == 3)
    print(CountZeros([0]) == 1)
    print(CountZeros([1, 0, 4, 5, 0, 6, 0]) == 3)
    print(CountZeros([1, 2, 3, 4]) == 0)
test_algo()    