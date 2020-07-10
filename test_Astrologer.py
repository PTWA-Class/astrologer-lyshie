import unittest
from Astrologer import *

class MyTestCase(unittest.TestCase):

    def test_get_each_number(self):

        self.assertListEqual(
            [1], get_each_number(1)
        )
        self.assertListEqual(
            [1, 2], get_each_number(12)
        )
        self.assertListEqual(
            [2, 1], get_each_number(21)
        )
        self.assertListEqual(
            [1, 4, 5], get_each_number(145)
        )
    def test_life_number(self):
        self.assertEqual(4, get_life_number(1995, 12, 13))
        self.assertEqual(3, get_life_number(1, 1, 1))
        self.assertEqual(5, get_life_number(101, 10, 11))
        self.assertEqual(8, get_life_number(2000, 12, 30))


    def test_constellation(self):

        self.assertEqual("獅子座", get_constellation(8, 16))
        self.assertEqual("處女座", get_constellation(8, 30))
        self.assertEqual("天蠍座", get_constellation(11, 1))
        self.assertEqual("天秤座", get_constellation(9, 28))
        self.assertEqual("水瓶座", get_constellation(2, 5))
        self.assertEqual("雙魚座", get_constellation(2, 29))


if __name__ == '__main__':
    unittest.main()
