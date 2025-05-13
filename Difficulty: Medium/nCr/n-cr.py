#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        fact = [1] * (n + 1)
        
        for i in range(2, n + 1):
            fact[i] = i * fact[i - 1]
            
        return fact[n]//(fact[r] * fact[n - r]) if n >= r else 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends