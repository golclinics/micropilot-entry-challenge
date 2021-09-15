def CountZeros(N):
    counter=0
    for num in N:
        #if any value is equal to zero -->count
        if num==0:
            counter+=1
    return counter 
def test_algo():
    print(CountZeros([0, 0, 0]) == 3)
    print(CountZeros([0]) == 1)
    print(CountZeros([1, 0, 4, 5, 0, 6, 6]) == 2)
    print(CountZeros([3,4,5,6]) == 0)
test_algo()   