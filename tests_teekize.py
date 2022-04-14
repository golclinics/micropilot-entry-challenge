"""
Includes test cases for the quadratic formula.
"""


import unittest


from teekize import getX


class TestQuadraticFormula(unittest.TestCase):
    """
    test all possible edge cases in the quadratic 
    function. 
    """
    def test_valid_ints(self):
        self.assertEqual(getX(1,4, -21), 3)

    def test_valid_floats(self):
        self.assertEqual(getX(1.0, 4.0,-21), 3)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            getX(2, "9", 2)

    def test_zero_a(self):
        with self.assertRaises(ValueError):
            getX(0, 9, 2)

    def test_negative_discriminant(self):
        self.assertEqual(getX(3, 4, 2), "Equation has no solution")

    def test_zero_discriminant(self):
        self.assertEqual(getX(1, 0, -0), (0))


if __name__ == '__main__':
    unittest.main()