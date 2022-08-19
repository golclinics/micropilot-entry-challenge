from cgi import test


def countZeros(arr):
    count = 0

    for num in arr:
        if num == 0:
            count += 1
    return count 

def testZeros():
    assert countZeros([1, 2, 3]) == 0
    assert countZeros([0, 2, 3]) == 1
    assert countZeros([0, 0, 0, 0, 0, 9]) == 5

if __name__ == "__main__":
    testZeros()
    print("Everything passed")