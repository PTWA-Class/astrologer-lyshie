import unittest
from Astrologer import *

class FormalTestCase(unittest.TestCase):

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
        self.assertListEqual(
            [3, 6, 9], get_each_number(369)
        )
        self.assertListEqual(
            [9, 6, 3], get_each_number(963)
        )
        self.assertListEqual(
            [9, 3, 6], get_each_number(936)
        )

    def test_life_number(self):
        self.assertEqual(4, get_life_number(1995, 12, 13))
        self.assertEqual(3, get_life_number(1, 1, 1))
        self.assertEqual(5, get_life_number(101, 10, 11))
        self.assertEqual(8, get_life_number(2000, 12, 30))
        self.assertEqual(9, get_life_number(1993, 8, 15))
        self.assertEqual(1, get_life_number(1993, 8, 16))
        self.assertEqual(6, get_life_number(1993, 8, 30))

    def test_constellation(self):
        self.assertEqual("魔羯座", get_constellation(1, 1))
        self.assertEqual("獅子座", get_constellation(8, 16))
        self.assertEqual("處女座", get_constellation(8, 30))
        self.assertEqual("天蠍座", get_constellation(11, 1))
        self.assertEqual("牡羊座", get_constellation(3, 21))
        self.assertEqual("金牛座", get_constellation(4, 30))
        self.assertEqual("巨蟹座", get_constellation(7, 9))
        self.assertEqual("天秤座", get_constellation(9, 28))
        self.assertEqual("射手座", get_constellation(11, 23))
        self.assertEqual("魔羯座", get_constellation(12, 24))
        self.assertEqual("水瓶座", get_constellation(2, 5))
        self.assertEqual("雙魚座", get_constellation(2, 29))


if __name__ == '__main__':
    unittest.main()
