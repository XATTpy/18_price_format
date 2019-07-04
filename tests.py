import unittest

from format_price import format_price

class QuadraticEquationTestCase(unittest.TestCase):
    def test_str_float_1(self):
        self.assertEqual(format_price('3000.0000'), '3 000')


    def test_str_float_2(self):
        self.assertEqual(format_price('3000.25330000000'), '3 000.25')


    def test_str_int(self):
        self.assertEqual(format_price('300000'), '300 000')


    def test_str_with_chars(self):
        self.assertEqual(format_price('TEST4'), None)


    def test_zero(self):
        self.assertEqual(format_price('0'), '0')


if __name__ == '__main__':
    unittest.main()
