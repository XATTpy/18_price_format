import unittest
from format_price import format_price


class QuadraticEquationTestCase(unittest.TestCase):

    def test_str_float_1(self):
        self.assertEqual(format_price('3000.0000'), '3 000')

    def test_str_float_2(self):
        self.assertEqual(format_price('3000.25330000000'), '3 000.25')

    def test_str_int_1(self):
        self.assertEqual(format_price('300000'), '300 000')

    def test_str_int_2(self):
        self.assertEqual(format_price('-300000'), '-300 000')

    def test_str_with_chars(self):
        self.assertEqual(format_price('TEST4'), None)

    def test_zero(self):
        self.assertEqual(format_price('0'), '0')

    def test_bool(self):
        self.assertAlmostEqual(format_price(True), None)

    def test_list(self):
        self.assertAlmostEqual(format_price((1, 2, 3, 5)), None)

    def test_array(self):
        self.assertAlmostEqual(format_price([1, 2, 'rfse', 4]), None)

    def test_dict(self):
        self.assertAlmostEqual(format_price({'1': 1}), None)

    def test_lambda(self):
        self.assertAlmostEqual(format_price(lambda x, y: x+y), None)


if __name__ == '__main__':
    unittest.main()
