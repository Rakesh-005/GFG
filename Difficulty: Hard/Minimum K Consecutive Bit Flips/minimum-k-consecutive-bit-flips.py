class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flips = 0
        flip_end = 0
        flip_count = 0

        for i in range(n):
            if i >= k and arr[i - k] == 2:
                flip_count ^= 1

            if (arr[i] ^ flip_count) == 0:
                if i + k > n:
                    return -1
                flips += 1
                flip_count ^= 1
                arr[i] = 2

        return flips

