import unittest
'''
Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. 
For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
'''

def count_zeros(A):
    count = 0

    for num in A:
        if num == 0:
            count += 1

    return count 

print(count_zeros([1, 0, 5, 6, 0, 2]))

class TestCountZeros(unittest.TestCase):

    def test_nozeros(self):
        self.assertEqual(count_zeros([1, 2, 3, 4, 5]), 0)

    def test_zeros(self):
        self.assertEqual(count_zeros([1, 0, 5, 6, 0, 2]), 2)

    def test_allzeros(self):
        self.assertEqual(count_zeros([0, 0, 0, 0, 0]), 5)

if __name__ == '__main__':
    unittest.main()