#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
        for i in range(n):
            if arr[i] > (k + i):
                return k + i
                
        return k + n

