from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        n, i, st, en = len(arr), 0, 0, 0
        mn, mx = deque(), deque()
        
        for j in range(n):
            while mn and mn[-1] > arr[j]: mn.pop()
            while mx and mx[-1] < arr[j]: mx.pop()
            mn.append(arr[j])
            mx.append(arr[j])
    
            while mx[0] - mn[0] > x:
                if arr[i] == mn[0]: mn.popleft()
                if arr[i] == mx[0]: mx.popleft()
                i += 1
    
            if j - i > en - st:
                st, en = i, j
    
        return arr[st:en+1] if en > st else [arr[0]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends