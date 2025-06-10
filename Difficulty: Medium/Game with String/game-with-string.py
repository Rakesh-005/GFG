class Solution:
    def minValue(self, s, k):
        # code here
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=list(d.values())
        for i in range(k):
            l.sort()
            l[-1]=l[-1]-1
        s=0
        for i in l:
            s+=i*i
        return s