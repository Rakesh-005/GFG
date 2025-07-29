class Solution:
    # Function to find the maximum profit
    def knapsack(self,W, val, wt):
        
        # Initializing dp list
        dp = [0] * (W + 1)
    
        # Taking first i elements
        for i in range(1, len(wt) + 1):
            
            # Starting from back, so that we also have data of
            # previous computation of i-1 items
            for j in range(W, wt[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])
        
        return dp[W]
