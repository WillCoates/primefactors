import unittest
from primefactors import factorize


class TestFactorize(unittest.TestCase):
    def test_factors_of_zero(self):
        self.assertEqual(factorize(0), [])

    def test_factors_of_one(self):
        self.assertEqual(factorize(1), [])

    def test_factors_of_two(self):
        self.assertEqual(factorize(2), [2])

    def test_factors_of_small_int(self):
        self.assertEqual(factorize(15), [3, 5])

    def test_repeated_factors(self):
        self.assertEqual(factorize(71672), [2, 2, 2, 17, 17, 31])
    
    def test_factors_of_medium_int(self):
        self.assertEqual(factorize(3825476), [2, 2, 17, 101, 557])

    def test_factors_of_large_int(self):
        self.assertEqual(factorize(246819835539726757), [7, 11, 37, 131, 557, 18379, 64601])

    def test_factors_maxint64(self):
        self.assertEqual(factorize(18446744073709551615), [3, 5, 17, 257, 641, 65537, 6700417])
    
    def test_factors_of_prime(self):
        self.assertEqual(factorize(13713779), [13713779])
    
    def test_factors_of_prime_int_squared(self):
        self.assertEqual(factorize(281476419553081), [16777259, 16777259])

if __name__ == '__main__':
    unittest.main()