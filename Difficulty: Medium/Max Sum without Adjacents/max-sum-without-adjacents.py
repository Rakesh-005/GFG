# User function Template for python3
class Solution:
    def findMaxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(arr[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]
