import unittest
from main import prime_v2 as prime


class PrimeTest(unittest.TestCase):
    def is_ok(self):
        for i in [1,2, 3, 5, 7, 11, 13, 17, 19]:
            self.assertTrue(prime(i))

    def is_ng(self):
        for i in [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]:
            self.assertFalse(prime(i))

    def is_negative(self):
        for i in [-1]:
            self.assertFalse(prime(i))

    def is_string(self):
        for i in ['a']:
            with self.assertRaises(TypeError):
                prime(i)


if __name__ == '__main__':
    unittest.main
