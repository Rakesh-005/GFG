#User function Template for python3
class Solution:
    def ncr(self,n,r):
        c=1
        for i in range(r):
            c*=(n-i)
            c//=(i+1)
        return c
    def nthRowOfPascalTriangle(self, n):
        # code here
        a=[]
        for i in range(n):
            a.append(self.ncr(n-1,i))
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends