import unittest
from practice_problems.sort.group_anagram import *

# Note that order of elements once grouped doesnt matter according the the problem
# So, these test cant be modified if your approach doesnt leave them in the exact
# Same order below but still grouped

# Describes approach where final array isn't sorted
class GroupAnagramTest(unittest.TestCase):
    def test_group_anagram_not_present(self):
        strings = ['tacos', 'burritos', 'cheese', 'whiskey']
        self.assertEqual(
            group_anagram(strings),
            strings
        )

    def test_group_anagram(self):
        strings = ['Elvis', 'Listen', 'Lives', 'Silent']
        expected = ['Elvis', 'Lives' , 'Listen', 'Silent']
        self.assertEqual(
            group_anagram(strings),
            expected
        )

    def test_group_anagram_with_spaces(self):
        strings = ['Clint Eastwood', 'Postmaster', 'Listen', 'Old West Action', 'Silent', 'Stamp Store']
        expected = ['Clint Eastwood', 'Old West Action', 'Postmaster', 'Stamp Store', 'Listen', 'Silent']
        self.assertEqual(
            group_anagram(strings),
            expected
        )

# Describes approach where final array is sorted
class SimpleGroupAnagramTest(unittest.TestCase):
    def test_group_anagram_not_present(self):
        strings = ['tacos', 'burritos', 'cheese', 'whiskey']
        self.assertEqual(
            simple_group_anagram(strings),
            strings
            )

    def test_group_anagram(self):
        strings = ['Elvis', 'Listen', 'Lives', 'Silent']
        expected = ['Listen', 'Silent', 'Elvis', 'Lives']
        self.assertEqual(
            simple_group_anagram(strings),
            expected
        )

    def test_group_anagram_with_spaces(self):
        strings = ['Clint Eastwood', 'Postmaster', 'Listen', 'Old West Action', 'Silent', 'Stamp Store']
        expected = ['Clint Eastwood', 'Old West Action', 'Postmaster', 'Stamp Store', 'Listen', 'Silent']
        self.assertEqual(
            simple_group_anagram(strings),
            expected
        )


if __name__ == '__main__':
    unittest.main()


# Hints
# No specific ordering of the words is required beyond grouping the anagrams
# Anagram is defined as two words with the same letters in different orders
