import unittest
from triple_step import *

class TripleStepTest(unittest.TestCase):
    def test_triple_step_1(self):
        stairs = 1
        self.assertEqual(
            triple_step(stairs),
            1
        )

    def test_triple_step_2(self):
        stairs = 2
        self.assertEqual(
            triple_step(stairs),
            2
        )

    def test_triple_step_3(self):
        stairs = 3
        self.assertEqual(
            triple_step(stairs),
            4
        )

    def test_triple_step_4(self):
        stairs = 4
        self.assertEqual(
            triple_step(stairs),
            7
        )

    def test_triple_step_5(self):
        stairs = 5
        self.assertEqual(
            triple_step(stairs),
            13
        )

    def test_triple_step_6(self):
        stairs = 6
        self.assertEqual(
            triple_step(stairs),
            24
        )


if __name__ == "__main__":
    unittest.main()
