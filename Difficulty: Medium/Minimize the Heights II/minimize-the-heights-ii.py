#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        n=len(arr)
        # Initial difference
        diff = arr[-1] - arr[0]
        
        # Traverse the array and adjust the heights
        for i in range(n - 1):
            max_height = max(arr[i] + k, arr[-1] - k)
            min_height = min(arr[0] + k, arr[i + 1] - k)
            if min_height < 0:  # Ensure heights are non-negative
                continue
            diff = min(diff, max_height - min_height)
        
        return diff

