#!/usr/bin/bash

def count_zeros(my_array):
    count = 0

    for num in my_array:
        if num == 0:
            count += 1
    return count

def test_count_zeros():
    assert count_zeros([1,0,2,0,3,0,4]) == 3, "Should be 3"
    assert count_zeros([4,5,7,5,3,0]) == 1, "Should be 1"
    assert count_zeros([2,5,4]) == 0, "Should be 0"

if __name__ == "__main__":
    test_count_zeros()
    print("Everything passed")