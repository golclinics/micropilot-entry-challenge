from count_zeros import  CountZeros
import unittest

class ZerosTestCase(unittest.TestCase):
    def test_count_zeros(self):
        result = CountZeros([1, 0, 5, 6, 0, 2])
        self.assertEqual(result,2)


if __name__ == '__main__':
    unittest.main()