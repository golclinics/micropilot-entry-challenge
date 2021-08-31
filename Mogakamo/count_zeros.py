from typing import List
def countZeros(list_of_int: List[int]) -> int:
     return list_of_int.count(0)

assert countZeros(([1,0,5,6,0,2,1]))== 2, "Number of zeros should be 2"
assert countZeros(([0,0,0,0,0,0,0]))== 7, "Number of zeros should be 7"
