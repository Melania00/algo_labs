class KthLargestElementFinder:
    def __init__(self, arr):
        self.arr = arr

    def k_largest(self, k):
        if len(self.arr) < k:
            return "Array size is smaller than k"

        sorted_arr = sorted(self.arr, reverse=True)  # Sort array
        k_largest = sorted_arr[k - 1]  # Get the kth largest element
        return k_largest

    # Find the position (index) of the kth largest element in the original array
    def position(self, k_largest):
        if k_largest in self.arr:
            position = self.arr.index(k_largest)
            return position
        else:
            return "There is no largest k in array"

