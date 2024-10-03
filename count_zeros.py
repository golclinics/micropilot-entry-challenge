def countZeros(A):
    count = 0
    #Iterate through the array
    for i in A:
        if i==0:
            count+=1
    return count

def test_countZeros():
    # Test cases
    assert countZeros([1, 0, 5, 6, 0, 2]) == 2, "First test case failed"
    assert countZeros([0, 0]) == 2, "Second test case failed"
    assert countZeros([1, 2]) == 0, "Third test case failed"
    assert countZeros([]) == 0, "Forth test case failed"
    assert countZeros([0]) == 1, "Fifth Test case failed"
    
    print("All test cases passed!")

test_countZeros()
