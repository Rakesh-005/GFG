#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
import heapq
class Solution:
    def replaceWithRank(self, N, arr):
        # Code here
        ra=1
        d={}
        l=[]
        for i in arr:
            heapq.heappush(l,i)
        while l:
            a=heapq.heappop(l)
            if a not in d:
                d[a]=ra
                ra+=1
        l2=[]
        for i in arr:
            l2.append(d[i])
        return l2
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.replaceWithRank(N, arr)
        for rank in res:
            print(rank, end = ' ')
        print()
        print("~")
# } Driver Code Ends