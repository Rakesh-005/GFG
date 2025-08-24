class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        n=len(arr)
        if n<(m*k):
            return -1
        return sorted(arr)[(m*k)-1]