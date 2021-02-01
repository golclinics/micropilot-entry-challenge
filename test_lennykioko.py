import unittest

from lennykioko import getX


class TestQuadraticFunction(unittest.TestCase):
    def test_valid_ints(self):
        self.assertEqual(getX(1, 5, -14), 2)

    def test_valid_floats(self):
        self.assertEqual(getX(1.0, 5.0, -14), 2)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            getX(1, "5", -14)

    def test_zero_a(self):
        with self.assertRaises(ValueError):
            getX(0, 5, -14)

    def test_negative_discriminant(self):
        self.assertEqual(getX(3, 4, 2), "Equation has no real solution")

    def test_zero_discriminant(self):
        self.assertEqual(getX(9, 12, 4), -(2/3))


if __name__ == '__main__':
    unittest.main()
