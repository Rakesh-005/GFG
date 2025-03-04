class Solution:
    def lis(self, arr):
        # code here
        dp = [1] * len(arr)
        for i in range(len(arr)):
            dp[i] = max([dp[j] for j in range(i) if arr[j] < arr[i]] + [0]) + 1
        return max(dp)



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends