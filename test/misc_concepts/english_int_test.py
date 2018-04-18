import unittest
from english_int import *

class EnglishIntTest(unittest.TestCase):
    def test_small_int_one(self):
        # pdb.set_trace()
        result = english_int(1)
        expected = "One"
        self.assertEqual(
            result,
            expected
        )

    def test_small_int_two(self):
        result = english_int(2)
        expected = "Two"
        self.assertEqual(
            result,
            expected
        )

    def test_int_ten(self):
        result = english_int(10)
        expected = "Ten"
        self.assertEqual(
            result,
            expected
        )

    def test_int_eleven(self):
        result = english_int(11)
        expected = "Eleven"
        self.assertEqual(
            result,
            expected
        )

    def test_int_fourteen(self):
        result = english_int(14)
        expected = "Fourteen"
        self.assertEqual(
            result,
            expected
        )

    def test_int_twenty(self):
        result = english_int(20)
        expected = "Twenty"
        self.assertEqual(
            result,
            expected
        )

    def test_int_twenty_one(self):
        result = english_int(21)
        expected = "Twenty One"
        self.assertEqual(
            result,
            expected
        )


    def test_int_twenty_five(self):
        result = english_int(25)
        expected = "Twenty Five"
        self.assertEqual(
            result,
            expected
        )

    def test_int_ninty_nine(self):
        result = english_int(99)
        expected = "Ninty Nine"
        self.assertEqual(
            result,
            expected
        )

    def test_int_one_hundred(self):
        result = english_int(100)
        expected = "One Hundred"
        self.assertEqual(
            result,
            expected
        )


    def test_int_one_hundred_and_one(self):
        result = english_int(101)
        expected = "One Hundred One"
        self.assertEqual(
            result,
            expected
        )


    def test_int_one_hundred_and_ten(self):
        result = english_int(110)
        expected = "One Hundred Ten"
        self.assertEqual(
            result,
            expected
        )

    def test_int_one_thousand(self):
        result = english_int(1000)
        expected = "One Thousand"
        self.assertEqual(
            result,
            expected
        )

    def test_int_one_thousand_and_one(self):
        result = english_int(1001)
        expected = "One Thousand One"
        self.assertEqual(
            result,
            expected
        )


    def test_int_one_thousand_one_hundred_one(self):
        result = english_int(1101)
        expected = "One Thousand One Hundred One"
        self.assertEqual(
            result,
            expected
        )



if __name__ == "__main__":
    unittest.main()
