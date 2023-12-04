import unittest
from src.kmp import KMP

class TestKMP(unittest.TestCase):
    def setUp(self):
        self.kmp = KMP()

    def test_compute_prefix_array(self):
        # Test cases for compute_prefix_array function
        self.assertEqual(self.kmp.compute_prefix_array("AABAACAABAA"), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])
        self.assertEqual(self.kmp.compute_prefix_array("ABCDE"), [0, 0, 0, 0, 0])
        self.assertEqual(self.kmp.compute_prefix_array("AAAAA"), [0, 1, 2, 3, 4])

    def test_search(self):
        # Test cases for search function
        haystack1 = "ABABDABACDABABCABAB"
        needle1 = "ABABCABAB"
        self.assertEqual(self.kmp.search_all(needle1, haystack1), [10])

        haystack2 = "AABAACAADAABAABA"
        needle2 = "AABA"
        self.assertEqual(self.kmp.search_all(needle2, haystack2), [0, 9, 12])

        haystack3 = "ABCDEF"
        needle3 = "XY"
        self.assertEqual(self.kmp.search_all(needle3, haystack3), [])

        haystack4 = "AAAAA"
        needle4 = "AA"
        self.assertEqual(self.kmp.search_all(needle4, haystack4), [0, 1, 2, 3])

    def test_empty_input(self):
        # Test cases for empty input
        haystack = "ABCD"
        needle = ""
        self.assertEqual(self.kmp.search_all(needle, haystack), [])
        self.assertEqual(self.kmp.search_all("A", ""), [])
        self.assertEqual(self.kmp.search_all("", ""), [])


if __name__ == "__main__":
    unittest.main()
