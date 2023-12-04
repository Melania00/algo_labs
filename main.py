from kmp import KMP


def main():
    kmp = KMP()
    haystack = input("Enter the haystack: ")
    needle = input("Enter the needle to search for: ")

    indices = kmp.search_all(needle, haystack)

    if indices:
        lps = []
        for index in indices:
            new_indices = [i for i in range(index, index + len(needle)) if i not in lps]
            lps.extend(new_indices)

        print(f"LPS array containing matched character indices: {lps}")
    else:
        print("The needle was not found in the haystack.")


if __name__ == "__main__":
    main()
