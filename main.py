from kmp import KMP

def main(self):
    haystack = input("Enter the haystack: ")
    needle = input("Enter the needle to search for: ")

    indices = self.search(needle, haystack)

    if indices:
        lps = [idx for idx in range(indices[0], indices[0] + len(needle))]
        print(f"LPS array containing matched character indices: {lps}")
    else:
        print("The needle was not found in the haystack.")


if __name__ == "__main__":
    kmp = KMP()
    kmp.main()
