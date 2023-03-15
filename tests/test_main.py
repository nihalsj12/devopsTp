import unittest
import main

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(3, 4), 7)
        self.assertEqual(main.add(-2, 5), 3)

    def test_subtract(self):
        self.assertEqual(main.subtract(7, 3), 4)
        self.assertEqual(main.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)
        self.assertEqual(main.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(main.divide(10, 5), 2)
        self.assertEqual(main.divide(-10, 2), -5)

        with self.assertRaises(ValueError):
            main.divide(5, 0)

if __name__ == '__main__':
    unittest.main()