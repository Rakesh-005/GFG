class Solution:
	def minJumps(self, arr):
	    # code here
        from collections import deque
        q = deque([(0, 0)])
        
        for i, e in enumerate(arr):
            while q and q[0][0] < i:
                q.popleft()
            if not q:
                return -1
            if i+e > q[0][0]:
                q.append((i+e, q[0][1]+1))
        return q[0][1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends