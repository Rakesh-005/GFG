class Solution:
    def missingNum(self, arr):
        # code here
        s=set(arr)
        i=1
        while i in s:
            i+=1
        return i