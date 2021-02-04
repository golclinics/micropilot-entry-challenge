import unittest
import Gakwandi 

class TestLargeNumber(unittest.TestCase):
    def test_large_number(self):
        self.assertEqual(Gakwandi.getX(2, -5, -3),3.0, "Should be 3.0")

if __name__ == "__main__":
    unittest.main()
