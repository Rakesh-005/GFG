#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        n=len(price)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]=max(dp[i],price[j-1]+dp[i-j])
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        # n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a))

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends