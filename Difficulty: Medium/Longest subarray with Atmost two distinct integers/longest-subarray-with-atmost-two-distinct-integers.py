class Solution:
    def totalElements(self, arr):
        from collections import defaultdict

        m = 0
        l = 0
        freq = defaultdict(int)

        for r in range(len(arr)):
            freq[arr[r]] += 1

            while len(freq) > 2:
                freq[arr[l]] -= 1
                if freq[arr[l]] == 0:
                    del freq[arr[l]]
                l += 1

            m = max(m, r - l + 1)

        return m
