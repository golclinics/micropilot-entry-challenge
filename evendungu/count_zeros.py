
from typing import Counter


def solution(A):
    counter = Counter(A)
    zeros =  counter.get(0) 
    if zeros == None:
        return 0
    else:
        return zeros
