import unittest
from count_zeros import count_zeros

class TestCountZeros(unittest.TestCase):
    def test_count_zeros(self):
        numbers = [1,0,5,6,0,2]        
        self.assertEqual(count_zeros(numbers), 2)


if __name__ == "__main__":
    unittest.main()
