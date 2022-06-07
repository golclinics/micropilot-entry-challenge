import count_zeros
import unittest

class TestCountZeros(unittest.TestCase):
    def test_count_zeros(self):
        A = [1, 0, 5, 6, 0, 2]
        B = [1, 0, 5, 6, 0, 2, 0]
        C = [1, 0, 5, 6, 0, 2, 0, 0]
        D = [1, 0, 5, 6, 0, 2, 0, 0, 0]
        E = [1, 0, 5, 6, 0, 2, 0, 0, 0, 0]
        self.assertEqual(count_zeros.CountZeros(A), 2)
        self.assertEqual(count_zeros.CountZeros(B), 3)
        self.assertEqual(count_zeros.CountZeros(C), 4)
        self.assertEqual(count_zeros.CountZeros(D), 5)
        self.assertEqual(count_zeros.CountZeros(E), 6)
