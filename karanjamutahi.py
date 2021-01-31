'''
Assumptions
The function will not handle complex roots
'''

import unittest
from math import sqrt

def getX(a,b,c):
    if a == 0:
        raise ValueError("Cannot Divide by zero")
    discriminant = (b*b) - (4*a*c)
    if discriminant < 0:
        raise ValueError("Will not compute negative roots")
    sqrt_discriminant = sqrt(discriminant)
    x1 = (-b-sqrt_discriminant) / (2*a)
    x2 = (-b+sqrt_discriminant) / (2*a)
    return max(x1, x2)

class Test(unittest.TestCase):
    def test_negative_discrminant(self):
        self.assertRaises(ValueError, getX, 4, 1, 9)
    def test_perfect_square(self):
        self.assertEqual(getX(1,6,9), -3.0)
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, getX, 0, 2, 2)
    def test_normal_test_case(self):
        self.assertEqual(getX(1,-3,-10), 5.0)



if __name__ == "__main__":
    unittest.main()

