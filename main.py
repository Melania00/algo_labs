from k_largest_element import KthLargestElementFinder

if __name__ == "__main__":
    arr = [15, 7, 22, 9, 36, 2, 42, 18]
    largest_k_finder = KthLargestElementFinder(arr)
    position_finder = KthLargestElementFinder(arr)

    k = 1
    k_largest = largest_k_finder.k_largest(k)
    position = position_finder.position(k_largest)

    if k_largest is not None:
        print(f"largest element: {k_largest}")
        print(f"position of largest element in array: {position}")
    else:
        print(f"incorrect value of k")
