import unittest

from count_zero import count_zero


class TestStringMethods(unittest.TestCase):

    def test_zero_len(self):
        self.assertEqual(count_zero([]), 0)

    def test_fix_zero(self):
        self.assertEqual(count_zero([0, 0, 0, 0, 0]), 5)

    def test_ten_zero(self):
        self.assertEqual(count_zero([1, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0]), 10)

    def test_zero_not_in_data(self):
        self.assertEqual(count_zero(range(1,50)), 0)


if __name__ == '__main__':
    unittest.main()
