class Solution:
    def substrCount(self, s, k):
        # code here
        l=0
        for i in range(0,len(s)-k+1):
            if len(set(s[i:i+k]))==k-1:
                l+=1
        return l
        