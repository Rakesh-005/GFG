class Solution:
    def missingNumber(self, arr):
        # code here
        a=1
        while a in set(arr):
            a+=1
        return a