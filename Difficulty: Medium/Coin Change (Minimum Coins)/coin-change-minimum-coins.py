class Solution:
	 def minCoins(self, coins, target):
        # code here
        def f(ind, target):
            if target == 0:
                return 0
            if ind >= n:
                return float('inf')
            if dp[ind][target] != -1:
                return dp[ind][target]
            p1 = float('inf')
            if target >= coins[ind]:
                p1 = 1 + f(ind, target - coins[ind])
            p2 = f(ind + 1, target)
            dp[ind][target] = min(p1, p2)
            return min(p1, p2)
        
        n = len(coins)
        coins.sort()
        dp = [[-1]*(target+1) for _ in range(n)]
        return f(0, target) if f(0, target) != float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends