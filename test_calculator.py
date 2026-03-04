import unittest
from calculator import add, subtract, multiply,divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def multiply(self):
        self.assertEqual(multiply(10, 4), 40)

    def divide(self):
        self.assertEqual(divide(10, 4), 10)
    
        

if __name__ == '__main__':
    unittest.main()
