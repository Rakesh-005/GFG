class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        # code here
        res = 0
    
        # Start and end pointer of the window
        start = 0
        end = 0
    
        # Counter to keep track of zeros in current window
        cnt = 0
    
        while end < len(arr):
            if arr[end] == 0:
                cnt += 1
    
            # Shrink the window from left if no. 
            # of zeroes are greater than k
            while cnt > k:
                if arr[start] == 0:
                    cnt -= 1
    
                start += 1
    
            res = max(res, (end - start + 1))
    
            # Increment the end pointer 
            # to expand the window
            end += 1
    
        return res


