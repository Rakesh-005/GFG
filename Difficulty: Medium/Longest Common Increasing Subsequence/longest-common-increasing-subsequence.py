class Solution:
    def LCIS(self, a, b):
        n, m = len(a), len(b)
        dp = [0] * m
        
        for i in range(n):
            current_max = 0
            for j in range(m):
                if a[i] > b[j]:
                    current_max = max(current_max, dp[j])
                elif a[i] == b[j]:
                    dp[j] = current_max + 1
        
        return max(dp)