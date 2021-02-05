import unittest

from salma_nyagaka import quadratic_equation


class TestQuadraticEquationFunction(unittest.TestCase):
    def test_valid_data(self):
        self.assertEqual(quadratic_equation(1, 10, -10),
                         'The larger value is 0.9160797830996161')

    def test_zero_sqrt(self):
        self.assertEqual(quadratic_equation(0, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()
