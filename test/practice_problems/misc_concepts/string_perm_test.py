import unittest
from itertools import *
from practice_problems.misc_concepts.string_perm import *

class StringPermTest(unittest.TestCase):
    def test_string_perm_simple(self):
        string = "abc"
        perms = string_perms(string, [])
        # expected_perms => ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        expected_perms = [ ''.join(i) for i in list(permutations(string)) ]
        for perm in perms:
            self.assertTrue(
                perm in expected_perms and len(perms) == 6
            )

    def test_string_perm_longer(self):
        string = "abcfg"
        perms = string_perms(string, [])
        # len(expected_perms) => 120
        expected_perms = [ ''.join(i) for i in list(permutations(string)) ]
        for perm in perms:
            self.assertTrue(
                perm in expected_perms and len(perms) == 120
            )

if __name__ == "__main__":
    unittest.main()
