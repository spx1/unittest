import unittest
from .basic import calc_factors

class TestBasic(unittest.TestCase):
    def test_not_null(self):
        self.assertIsNotNone(calc_factors(3))

    def test_calc_factors(self):
        self.assertEqual(calc_factors(27),[1,3,9,27])
