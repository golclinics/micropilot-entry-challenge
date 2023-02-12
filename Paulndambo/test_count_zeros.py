from unittest import TestCase
from count_zeros import CountZeros

class TestCountZerosFunction(TestCase):
    def test_count_zero_should_return_int(self):
        A = [1, 0, 0, 3, 4]
        zeros_count = CountZeros(A)
        self.assertIsInstance(zeros_count, int)


    def test_count_zero_should_return_correct_value(self):
        A = [1, 0, 0, 3, 4]
        zeros_count = CountZeros(A)
        self.assertEqual(zeros_count, 2)
