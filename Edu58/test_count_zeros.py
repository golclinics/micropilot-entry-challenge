import unittest
from count_zeros import CountZeros

class TestCountZeros(unittest.TestCase):
    def test_returns_correct_number_of_zeros(self):
        """
        Test if can return number of zeros
        """
        data = [2,5,86,0,45,0,456,0,4564,5,15,0,3]
        result = CountZeros(data)

        self.assertEqual(result, 4)

    def test_raises_value_error(self):
        """
        Test if it raises a value error if invalid type of data is provided
        """
        data = 2,4,5,0,8,6,0,0,6,0
        CountZeros(data)

        self.assertRaises(ValueError)



if __name__ == '__main__':
    unittest.main()