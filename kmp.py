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

    def search_all(self, pattern, text):
        if not pattern or not text:
            return 0

        prefix = self.compute_prefix_array(pattern)
        matches = []
        j = 0

        i = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j == len(pattern):
                    matches.append(i - j)
                    j = prefix[j - 1]
            else:
                if j != 0:
                    j = prefix[j - 1]
                else:
                    i += 1

        return matches
