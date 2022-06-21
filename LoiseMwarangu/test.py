import unittest
from count_zeros import count_zeros

class Testcount_zeros(unittest.TestCase):
    def testA(self):
        """
        test that count_zeros returns number of zeros
        """
        A= [1, 0, 5, 6, 0, 2]
        self.assertEqual(count_zeros(A), 2)
    def testB(self):
        """
        test that count_zeros does not consider strings
        """
        A = [1,'0',0,0,0,0,0,0,0,0]
        self.assertEqual(count_zeros(A), 8)    

if __name__ == '__main__':
    unittest.main()
