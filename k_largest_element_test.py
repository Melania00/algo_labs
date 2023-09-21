import unittest
from k_largest_element import KthLargestElementFinder


class TestKthLargestElementFinder(unittest.TestCase):
    def setUp(self):
        self.arr = [15, 7, 22, 9, 36, 2, 42, 18]
        self.largest_k_finder = KthLargestElementFinder(self.arr)
        self.position_finder = KthLargestElementFinder(self.arr)

    def test_k_largest(self):
        self.assertEqual(self.largest_k_finder.k_largest(1), 42)
        self.assertEqual(self.largest_k_finder.k_largest(2), 36)
        self.assertEqual(self.largest_k_finder.k_largest(3), 22)
        self.assertEqual(self.largest_k_finder.k_largest(8), 2)  # Smallest element
        self.assertEqual(self.largest_k_finder.k_largest(10), "Array size is smaller than k")  # Invalid k

    def test_position(self):
        self.assertEqual(self.position_finder.position(42), 6)
        self.assertEqual(self.position_finder.position(36), 4)
        self.assertEqual(self.position_finder.position(22), 2)
        self.assertEqual(self.position_finder.position(2), 5)
        self.assertEqual(self.position_finder.position(99), "There is no largest k in array")
        # Element not in the array


if __name__ == "__main__":
    unittest.main()
