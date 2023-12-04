class KMP:
    def compute_prefix_array(self, pattern):
        prefix_arr = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix_arr[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
            prefix_arr[i] = j

        return prefix_arr

    def search(self, pattern, text):
        if not pattern or not text:
            return []

        prefix = self.compute_prefix_array(pattern)
        matches = []
        j = 0

        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = prefix[j - 1]

            if text[i] == pattern[j]:
                j += 1

            if j == len(pattern):
                matches.append(i - j + 1)
                j = prefix[j - 1]

        return matches
