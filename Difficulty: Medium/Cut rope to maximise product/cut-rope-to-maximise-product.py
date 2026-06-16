class Solution:
    def maxProduct(self,n):
        # code here
        
        if n < 4:
            
            return n-1
            
        res = 1
        
        dp = [0] * (n+1)
        
        dp[0] = 0
        
        dp[1] = 0
        
        dp[2] = 1
        
        dp[3] =2
        
        dp[4] = 4
        
        
        for i in range(5, n+1):
            
            dp[i] = 0
            
            for j in range(1, i):
                
                dp[i] = max(dp[i], j*(i-j),  j*dp[i-j])
        #print(dp)
                
                
        return dp[n]