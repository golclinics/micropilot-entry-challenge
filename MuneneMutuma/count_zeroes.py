#!/usr/bin/env python3

def CountZeroes(A):
    count = 0
    for element in A:
        if element == 0:
            count += 1

    return count
