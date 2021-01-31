import unittest
import getX
from math import sqrt


def getX(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        num_roots = 2
        x1 = (((-b) + sqrt(discriminant)) / (2 * a))
        x2 = (((-b) - sqrt(discriminant)) / (2 * a))
        if x1 > x2:
            larger = x1
        else:
            larger = x2
        return larger

    elif discriminant == 0:
        num_roots = 1
        x = (-b) / 2 * a
        return x
    else:
        num_roots = 0
        return None


class TestRoots(unittest.TestCase):
    def test_returns_larger_root(self):
        result = getX(2, -5, 3)
        self.assertEqual(result, 1.5)

    def test_argument_a_is_zero(self):
        self.assertRaises(ZeroDivisionError, getX, 0, -2, 5)

    def test_discriminant_is_zero(self):
        result = getX(4, -12, 9)
        self.assertEqual(result, 24)

    def test_discriminant_is_less_than_zero(self):
        result=getX(3,1,9)
        self.assertEqual(result,None)


if __name__ == '__main__':
    unittest.main()
