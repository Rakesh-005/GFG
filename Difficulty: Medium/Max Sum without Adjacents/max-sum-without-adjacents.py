#User function Template for python3
def d(i,arr,dp):
    if i==0:
        return arr[i]
    if i<0:
        return 0
    if dp[i]!=-1:
        return dp[i]
    take=arr[i]+d(i-2,arr,dp)
    ntake=d(i-1,arr,dp)
    dp[i]=max(take,ntake)
    return dp[i]
    
class Solution:
	
	def findMaxSum(self,arr):
		# code here
		n=len(arr)
		dp=[-1]*n
		return d(n-1,arr,dp)
		