import unittest

from format_price import format_price

class QuadraticEquationTestCase(unittest.TestCase):
    def test_str_float_1(self):
        self.assertEqual(format_price('3000.0000'), '3 000')


    def test_str_float_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
