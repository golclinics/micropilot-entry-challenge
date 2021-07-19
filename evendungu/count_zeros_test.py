from count_zeros import solution

def test_solution():
    assert solution([1, 0, 5, 6, 0, 2]) == 2
    assert solution([1, 7, 5, 6, 9, 2]) == 0
    assert solution([]) == 0
