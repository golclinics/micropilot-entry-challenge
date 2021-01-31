import  manulangat1
import math 
import unittest



print(manulangat1.getX(1,-2,-3))


class TestRoot(unittest.TestCase):
    def test_discrimanant_less_than_zero(self):
        result = manulangat1.getX(3,1,9)
        self.assertEqual(result,"Oops! cannot find square root of a negative number!!")
    def test__arg_a_is_zero(self):
        result = manulangat1.getX(0,1,2)
        self.assertEqual(result,"Zero division error")
    def test_returns_largest_root(self):
        result = manulangat1.getX(1,-8,-10)
        self.assertEqual(result,9.099019513592784)


if __name__ == "__main__":
    unittest.main()


