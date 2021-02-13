import unittest
from count_zeros import CountZeros

class TestCountZero(unittest.TestCase):
  def test_count_zeros(self):
    numbers = [1, 0, 5, 6, 0, 2]
    self.assertEqual(CountZeros(numbers), 2)

  def test_invalid_data(self):
    numbers = 'invalid data type'
    with self.assertRaises(TypeError):
      CountZeros(numbers)

if __name__ == '__main__':
  unittest.main()
